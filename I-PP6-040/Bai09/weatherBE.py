from datetime import datetime
from weatherAPI import WeatherAPIClient

class WeatherService:
    def __init__(self):
        self.api_client = WeatherAPIClient()

    def _format_timestamp(self, ts: int) -> str:
        """Chuyển đổi timestamp Unix sang định dạng ngày tháng dễ đọc."""
        return datetime.fromtimestamp(ts).strftime('%A, %b %d')

    def get_weather_dashboard_data(self, city_name: str):
        """
        Hàm chính để lấy dữ liệu cho Frontend.
        Trả về một dictionary chứa data đã được format sẵn hoặc thông báo lỗi.
        """
        # 1. Lấy toạ độ
        location = self.api_client.get_coordinates(city_name)
        if not location:
            return {"error": f"Không tìm thấy toạ độ cho thành phố: {city_name}"}

        lat, lon = location['lat'], location['lon']
        city_display_name = f"{location['name']}, {location['country']}"

        # 2. Lấy dữ liệu thời tiết
        raw_data = self.api_client.get_weather_data(lat, lon)
        if not raw_data:
            return {"error": "Lỗi khi kết nối đến OpenWeatherMap API."}

        # 3. Trích xuất và format dữ liệu
        try:
            current = raw_data['current']
            forecast = raw_data['forecast']
            
            # Xử lý 2.5 forecast (3-hour intervals). Lấy 1 bản ghi mỗi ngày (vào khoảng giữa trưa).
            daily_forecast = []
            seen_dates = set()
            for item in forecast['list']:
                # Lấy ngày hiện tại
                date_str = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
                
                # Chỉ lấy 1 bản ghi mỗi ngày (ưu tiên khoảng 12:00) hoặc lấy bản ghi đầu tiên trong ngày nếu chưa có
                if date_str not in seen_dates:
                   # Nếu là 12:00, hoặc nếu chưa có bản ghi nào cho ngày này (phòng khi không có 12:00)
                   if '12:00:00' in item['dt_txt'] or len(seen_dates) == 0 or True: 
                       # Thực tế, để đơn giản cho Option A, ta lấy bản ghi đầu tiên của mỗi ngày mới xuất hiện
                       seen_dates.add(date_str)
                       daily_forecast.append(item)
                
                if len(daily_forecast) >= 5: # API này tối đa 5 ngày
                    break

            formatted_daily = []
            for day in daily_forecast:
                formatted_daily.append({
                    "date": self._format_timestamp(day['dt']),
                    "min_temp": round(day['main']['temp_min'], 1),
                    "max_temp": round(day['main']['temp_max'], 1),
                    "description": day['weather'][0]['description'].capitalize(),
                    "icon": day['weather'][0]['icon']
                })

            result = {
                "location_name": city_display_name,
                "current": {
                    "temp": round(current['main']['temp'], 1),
                    "feels_like": round(current['main']['feels_like'], 1),
                    "humidity": current['main']['humidity'],
                    "wind_speed": current['wind']['speed'],
                    "description": current['weather'][0]['description'].capitalize(),
                    "icon": current['weather'][0]['icon']
                },
                "daily": formatted_daily
            }
            return result

        except KeyError as e:
            return {"error": f"Dữ liệu API trả về không đúng định dạng. Thiếu key: {e}"}
