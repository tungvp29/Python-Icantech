import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

class WeatherAPIClient:
    def __init__(self):
        self.api_key = OPENWEATHER_API_KEY
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY not found in environment variables.")
        self.geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
        self.current_url = "https://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_coordinates(self, city_name: str):
        """Lấy toạ độ (lat, lon) từ tên thành phố."""
        params = {
            "q": city_name,
            "appid": self.api_key,
            "limit": 1
        }
        try:
            response = requests.get(self.geocoding_url, params=params)
            response.raise_for_status()
            data = response.json()
            if not data:
                return None
            
            return {
                "name": data[0].get("name"),
                "lat": data[0].get("lat"),
                "lon": data[0].get("lon"),
                "country": data[0].get("country")
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching coordinates: {e}")
            return None

    def get_weather_data(self, lat: float, lon: float, units: str = "metric"):
        """Lấy dữ liệu thời tiết hiện tại và dự báo 5 ngày từ One OpenWeatherMap."""
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": units
        }
        try:
            print(self.current_url, params)
            current_response = requests.get(self.current_url, params=params)
            current_response.raise_for_status()
            current_data = current_response.json()

            forecast_response = requests.get(self.forecast_url, params=params)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()

            return {
                "current": current_data,
                "forecast": forecast_data
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
