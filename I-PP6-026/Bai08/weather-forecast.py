#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Streamlit Weather App
- Lấy dữ liệu từ OpenWeatherMap (One Call 3.0 + Geocoding)
- Hiển thị thời tiết tuần gần nhất (tối đa 7 ngày, phụ thuộc gói API - có thể chỉ lấy được ~5 ngày gần nhất ở gói free)
- Dự báo cho tuần tiếp theo (7-8 ngày tới)

Hướng dẫn API Key:
- Tạo tài khoản và lấy API Key tại https://openweathermap.org/
- Cách cung cấp API key cho app:
  1) Đặt biến môi trường: export OPENWEATHER_API_KEY="<your_key>"
  2) Hoặc thêm vào .streamlit/secrets.toml: OPENWEATHER_API_KEY = "<your_key>"
  3) Hoặc nhập trực tiếp ở sidebar khi chạy app

Chạy ứng dụng:
  streamlit run weather-forecast.py
"""

import os
import time
import math
import datetime as dt
from typing import Dict, Any, List, Optional, Tuple

import requests
import pandas as pd
import streamlit as st

# ==========================
# Cấu hình trang
# ==========================
st.set_page_config(
    page_title="Dự báo thời tiết tuần",
    page_icon="⛅",
    layout="wide",
)

# ==========================
# Utils & API helpers
# ==========================
@st.cache_data(show_spinner=False)
def get_api_key_from_env_or_secrets() -> Optional[str]:
    # Ưu tiên st.secrets
    key = None
    try:
        key = st.secrets.get("OPENWEATHER_API_KEY", None)  # type: ignore[attr-defined]
    except Exception:
        key = None
    if not key:
        key = os.environ.get("OPENWEATHER_API_KEY")
    return key

@st.cache_data(show_spinner=False)
def geocode_city(city: str, api_key: str, limit: int = 1) -> Optional[Dict[str, Any]]:
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city, "limit": limit, "appid": api_key}
    r = requests.get(url, params=params, timeout=15)
    if r.status_code != 200:
        raise RuntimeError(f"Geocoding lỗi: HTTP {r.status_code} {r.text}")
    data = r.json()
    if not data:
        return None
    return data[0]

@st.cache_data(show_spinner=False)
def reverse_geocode(lat: float, lon: float, api_key: str) -> Optional[str]:
    url = "https://api.openweathermap.org/geo/1.0/reverse"
    params = {"lat": lat, "lon": lon, "limit": 1, "appid": api_key}
    r = requests.get(url, params=params, timeout=15)
    if r.status_code != 200:
        return None
    data = r.json()
    if data:
        name = data[0].get("name")
        country = data[0].get("country")
        state = data[0].get("state")
        pretty = name or ""
        if state:
            pretty += f", {state}"
        if country:
            pretty += f", {country}"
        return pretty or None
    return None

@st.cache_data(show_spinner=False)
def fetch_onecall(lat: float, lon: float, api_key: str, units: str = "metric", lang: str = "vi") -> Dict[str, Any]:
    """Lấy current + daily forecast (7-8 ngày tới) bằng One Call 3.0.
    Nếu 'daily' không có, trả về dict rỗng phần đó.
    """
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units,
        "lang": lang,
        "exclude": "minutely,alerts",
    }
    r = requests.get(url, params=params, timeout=20)
    if r.status_code != 200:
        raise RuntimeError(f"One Call lỗi: HTTP {r.status_code} {r.text}")
    return r.json()

@st.cache_data(show_spinner=False)
def fetch_timemachine(lat: float, lon: float, dt_unix: int, api_key: str, units: str = "metric", lang: str = "vi") -> Optional[Dict[str, Any]]:
    """Lấy dữ liệu lịch sử cho 1 ngày (theo timestamp). Theo gói free, có thể chỉ lấy được tới ~5 ngày trước.
    Trả về dữ liệu dạng hourly; có thể có key 'data' hoặc 'hourly' tùy phiên bản.
    """
    url = "https://api.openweathermap.org/data/3.0/onecall/timemachine"
    params = {
        "lat": lat,
        "lon": lon,
        "dt": dt_unix,
        "appid": api_key,
        "units": units,
        "lang": lang,
    }
    r = requests.get(url, params=params, timeout=20)
    if r.status_code != 200:
        # Có thể quá xa giới hạn lịch sử của gói free
        return None
    return r.json()

# ==========================
# Xử lý dữ liệu
# ==========================

def kelvin_to_c_if_needed(val: Optional[float], units: str) -> Optional[float]:
    if val is None:
        return None
    return float(val)


def aggregate_hourly_to_daily(hourly: List[Dict[str, Any]], units: str = "metric") -> Dict[str, Any]:
    """Tổng hợp hourly thành chỉ số theo ngày."""
    temps = []
    humid = []
    winds = []
    rains = []
    snows = []
    descs = []

    for h in hourly:
        main = h.get("main", {})
        temp = h.get("temp") or main.get("temp")
        humidity = h.get("humidity") or main.get("humidity")
        wind_speed = h.get("wind_speed") or (h.get("wind", {}).get("speed") if isinstance(h.get("wind"), dict) else None)
        weather = h.get("weather", [{}])[0]
        desc = weather.get("description")
        rain = 0.0
        snow = 0.0
        if isinstance(h.get("rain"), dict):
            rain = float(h["rain"].get("1h") or h["rain"].get("3h") or 0.0)
        if isinstance(h.get("snow"), dict):
            snow = float(h["snow"].get("1h") or h["snow"].get("3h") or 0.0)

        if temp is not None:
            temps.append(float(temp))
        if humidity is not None:
            humid.append(float(humidity))
        if wind_speed is not None:
            winds.append(float(wind_speed))
        rains.append(rain)
        snows.append(snow)
        if desc:
            descs.append(desc)

    summary = {
        "temp_min": min(temps) if temps else None,
        "temp_max": max(temps) if temps else None,
        "temp_avg": sum(temps) / len(temps) if temps else None,
        "humidity_avg": sum(humid) / len(humid) if humid else None,
        "wind_avg": sum(winds) / len(winds) if winds else None,
        "rain_sum": sum(rains) if rains else None,
        "snow_sum": sum(snows) if snows else None,
        "top_desc": pd.Series(descs).mode().iloc[0] if descs else None,
    }
    return summary


def build_daily_df_from_history(lat: float, lon: float, api_key: str, days: int, units: str = "metric", lang: str = "vi", sleep_each: float = 1.0) -> pd.DataFrame:
    """Lấy dữ liệu lịch sử theo ngày (tối đa 7 ngày; gói free có thể chỉ được 5 ngày).
    Trả về DataFrame với mỗi dòng là một ngày.
    """
    rows: List[Dict[str, Any]] = []
    now = dt.datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)

    for i in range(1, days + 1):
        day = now - dt.timedelta(days=i)  # 1..days ngày trước
        ts = int(day.timestamp())
        data = fetch_timemachine(lat, lon, ts, api_key, units=units, lang=lang)
        if not data:
            # Có thể vượt quá giới hạn lịch sử, bỏ qua và tiếp tục
            continue
        # API 3.0 có thể trả về 'data' (hourly) hoặc 'hourly'
        hourly = data.get("data") or data.get("hourly") or []
        if not isinstance(hourly, list) or len(hourly) == 0:
            continue
        summary = aggregate_hourly_to_daily(hourly, units=units)
        rows.append({
            "date": day.date(),
            **summary,
        })
        time.sleep(sleep_each)  # tránh vượt rate limit

    if not rows:
        return pd.DataFrame(columns=[
            "date","temp_min","temp_max","temp_avg","humidity_avg","wind_avg","rain_sum","snow_sum","top_desc"
        ])

    df = pd.DataFrame(rows).sort_values("date")
    return df


def build_daily_df_from_forecast(daily_list: List[Dict[str, Any]]) -> pd.DataFrame:
    rows = []
    for d in daily_list:
        day = dt.datetime.utcfromtimestamp(int(d.get("dt", 0))).date()
        temp = d.get("temp", {})
        weather = (d.get("weather") or [{}])[0]
        rows.append({
            "date": day,
            "temp_min": temp.get("min"),
            "temp_max": temp.get("max"),
            "temp_day": temp.get("day"),
            "humidity": d.get("humidity"),
            "wind_speed": d.get("wind_speed"),
            "rain": d.get("rain"),
            "snow": d.get("snow"),
            "desc": weather.get("description"),
            "icon": weather.get("icon"),
        })
    df = pd.DataFrame(rows).sort_values("date")
    return df

# ==========================
# UI
# ==========================
st.title("⛅ Ứng dụng thời tiết: Tuần trước & Tuần tới")

with st.sidebar:
    st.header("Cài đặt")

    default_city = "Ho Chi Minh, VN"
    city_mode = st.radio("Chọn cách nhập địa điểm", ["Tên thành phố", "Toạ độ (lat, lon)"])

    lat = lon = None
    city_input = None
    if city_mode == "Tên thành phố":
        city_input = st.text_input("Tên thành phố (VD: Ho Chi Minh, VN)", value=default_city)
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            lat = st.number_input("Vĩ độ (lat)", value=10.7769, format="%.4f")
        with col_b:
            lon = st.number_input("Kinh độ (lon)", value=106.7009, format="%.4f")

    units = st.selectbox("Đơn vị nhiệt độ", options=["metric", "imperial"], index=0, help="metric = °C, imperial = °F")
    lang = st.selectbox("Ngôn ngữ mô tả", options=["vi", "en"], index=0)

    api_key_default = get_api_key_from_env_or_secrets() or ""
    api_key_input = st.text_input("OpenWeather API Key", type="password", value=api_key_default)

    days_history = st.slider("Số ngày lịch sử (tuần gần nhất)", min_value=3, max_value=7, value=7)

    run_btn = st.button("Lấy dữ liệu")

# Gợi ý cấu hình API Key
if not api_key_input:
    st.info(
        "Chưa có API Key. Hãy nhập ở sidebar, hoặc đặt biến môi trường OPENWEATHER_API_KEY, hoặc thêm vào .streamlit/secrets.toml"
    )

# Khi bấm chạy
if run_btn and api_key_input:
    try:
        # Xác định toạ độ
        if city_mode == "Tên thành phố":
            geo = geocode_city(city_input, api_key_input) if city_input else None  # type: ignore[arg-type]
            if not geo:
                st.error("Không tìm thấy thành phố. Vui lòng thử lại.")
                st.stop()
            lat = float(geo["lat"])  # type: ignore[assignment]
            lon = float(geo["lon"])  # type: ignore[assignment]
            location_name = f"{geo.get('name', city_input)}{', ' + geo.get('country','') if geo.get('country') else ''}"
        else:
            assert lat is not None and lon is not None
            name = reverse_geocode(lat, lon, api_key_input)
            location_name = name or f"({lat:.4f}, {lon:.4f})"

        st.subheader(f"📍 Vị trí: {location_name}")
        st.map(pd.DataFrame([{"lat": lat, "lon": lon}]))  # type: ignore[arg-type]

        cols = st.columns(2)
        with cols[0]:
            st.markdown("### 🔮 Dự báo tuần tới")
        with cols[1]:
            st.markdown("### ⏪ Tuần vừa qua (lịch sử)")

        # Lấy One Call (current + daily)
        with st.spinner("Đang lấy dự báo tuần tới..."):
            onecall = fetch_onecall(lat, lon, api_key_input, units=units, lang=lang)  # type: ignore[arg-type]

        # Hiển thị hiện tại
        current = onecall.get("current", {})
        if current:
            c_temp = current.get("temp")
            c_hum = current.get("humidity")
            c_wind = current.get("wind_speed")
            c_weather = (current.get("weather") or [{}])[0]
            c_desc = c_weather.get("description")
            c_icon = c_weather.get("icon")

            cc1, cc2, cc3, cc4 = st.columns(4)
            with cc1:
                st.metric("Nhiệt độ hiện tại", f"{c_temp}°{'C' if units=='metric' else 'F'}")
            with cc2:
                st.metric("Độ ẩm", f"{c_hum}%")
            with cc3:
                st.metric("Gió", f"{c_wind} m/s")
            with cc4:
                if c_icon:
                    st.image(f"https://openweathermap.org/img/wn/{c_icon}@2x.png", width=64)
                st.caption(c_desc or "")

        # Dự báo daily
        daily = onecall.get("daily", [])
        if not daily:
            st.warning("API không trả về 'daily'. Có thể gói hiện tại không hỗ trợ daily forecast.")
        else:
            df_forecast = build_daily_df_from_forecast(daily)
            st.dataframe(
                df_forecast[["date","temp_min","temp_max","temp_day","humidity","wind_speed","desc"]]
                .rename(columns={
                    "date":"Ngày","temp_min":"Min","temp_max":"Max","temp_day":"Ban ngày","humidity":"Độ ẩm","wind_speed":"Gió","desc":"Mô tả"
                }),
                use_container_width=True,
            )
            # Biểu đồ nhiệt độ
            chart_df = df_forecast.set_index("date")[ ["temp_min","temp_day","temp_max"] ]
            st.line_chart(chart_df, height=280)

        # Lịch sử tuần qua (tối đa 7 ngày)
        with st.spinner("Đang lấy dữ liệu tuần vừa qua (có thể mất 3-10 giây)..."):
            df_history = build_daily_df_from_history(lat, lon, api_key_input, days=days_history, units=units, lang=lang)  # type: ignore[arg-type]
        if df_history.empty:
            st.warning("Không thể lấy đủ dữ liệu lịch sử 7 ngày. Gói free có thể chỉ cho ~5 ngày. Đã bỏ qua các ngày ngoài giới hạn.")
        else:
            st.dataframe(
                df_history.rename(columns={
                    "date":"Ngày","temp_min":"Min","temp_max":"Max","temp_avg":"Trung bình","humidity_avg":"Độ ẩm TB","wind_avg":"Gió TB","rain_sum":"Mưa (mm)","snow_sum":"Tuyết (mm)","top_desc":"Mô tả thường gặp"
                }),
                use_container_width=True,
            )
            # Biểu đồ min/max/avg
            chart_hist = df_history.set_index("date")[ ["temp_min","temp_avg","temp_max"] ]
            st.line_chart(chart_hist, height=280)

        st.info("Lưu ý: Dữ liệu lịch sử phụ thuộc gói API. Nếu không đủ 7 ngày, ứng dụng sẽ hiển thị những ngày có sẵn.")

    except Exception as e:
        st.error(f"Lỗi: {e}")
        st.exception(e)

else:
    st.caption("Nhập API key và địa điểm ở sidebar, sau đó bấm 'Lấy dữ liệu'.")
