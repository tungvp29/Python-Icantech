import streamlit as st
from weatherBE import WeatherService
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Minimalist Weather", page_icon="⛅", layout="centered")

def get_weather_icon_url(icon_code: str) -> str:
    """Return URL for OpenWeatherMap icon."""
    return f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

def render_dashboard():
    # Header
    st.title("🌦️ Minimalist Weather Dashboard")
    st.markdown("Tra cứu thời tiết hiện tại và dự báo 5 ngày theo kiến trúc 3 lớp.")
    
    # Input
    col1, col2 = st.columns([3, 1])
    with col1:
        city_input = st.text_input("Nhập tên thành phố (VD: Hanoi, Tokyo):", placeholder="Hanoi...")
    with col2:
        st.write("") # Spacer align button
        st.write("")
        submit = st.button("Tra cứu", use_container_width=True)

    # Styling for error messages
    st.markdown("""
        <style>
        .error-msg {
            color: #d32f2f;
            background-color: #ffebee;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    if submit and city_input:
        with st.spinner(f"Đang tìm thời tiết cho **{city_input}**..."):
            service = WeatherService()
            data = service.get_weather_dashboard_data(city_input)

            if "error" in data:
                st.markdown(f"<div class='error-msg'>⚠️ {data['error']}</div>", unsafe_allow_html=True)
            else:
                # 1. Current Weather Section
                st.divider()
                st.subheader(f"📍 {data['location_name']}")
                
                # Biểu diễn theo dạng Card lớn
                current = data['current']
                
                # Image icon and big temp
                col_icon, col_temp, col_desc = st.columns([1, 2, 2])
                with col_icon:
                    st.image(get_weather_icon_url(current['icon']), width=100)
                with col_temp:
                    st.metric("Nhiệt độ hiện tại", f"{current['temp']}°C", f"Cảm giác như: {current['feels_like']}°C")
                with col_desc:
                    st.metric("Trạng thái", current['description'])

                # Metrics khác
                m_col1, m_col2 = st.columns(2)
                with m_col1:
                    st.metric("💧 Độ ẩm", f"{current['humidity']}%")
                with m_col2:
                    st.metric("💨 Sức gió", f"{current['wind_speed']} m/s")

                # 2. Daily Forecast Section (5 days)
                st.divider()
                st.subheader("📅 Dự báo 5 Ngày Tới")
                
                daily_data = data['daily']
                
                # Sử dụng expander cho từng ngày hoặc hiển thị list
                for day in daily_data:
                    d_col1, d_col2, d_col3, d_col4 = st.columns([2, 1, 2, 2])
                    with d_col1:
                        st.write(f"**{day['date']}**")
                    with d_col2:
                        st.image(get_weather_icon_url(day['icon']), width=40)
                    with d_col3:
                        st.write(day['description'])
                    with d_col4:
                        st.write(f"🌡️ {day['min_temp']}°C - {day['max_temp']}°C")
                    st.markdown("---") # separator line
                    
    elif submit and not city_input:
        st.warning("Vui lòng nhập tên thành phố.")

if __name__ == "__main__":
    render_dashboard()
