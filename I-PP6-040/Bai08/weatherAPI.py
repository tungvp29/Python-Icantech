import os

class WeatherAPIClient:
    def __init__(self):
        pass

    def get_coordinates(self, city_name: str):
        """Lấy toạ độ (lat, lon) từ tên thành phố."""
        return {
            "name": "Hanoi",
            "lat": 21.0294498,
            "lon": 105.8544441,
            "country": "VN"
        }

    def get_weather_data(self, lat: float, lon: float, units: str = "metric"):
        """Lấy dữ liệu thời tiết hiện tại và dự báo 5 ngày từ One OpenWeatherMap."""
        
        current_data = {
            "coord": {
                "lon": 105.854,
                "lat": 21.0283
            },
            "weather": [
                {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 23.98,
                "feels_like": 24.29,
                "temp_min": 23.98,
                "temp_max": 23.98,
                "pressure": 1017,
                "humidity": 71,
                "sea_level": 1017,
                "grnd_level": 1016
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.43,
                "deg": 132,
                "gust": 4.63
            },
            "clouds": {
                "all": 97
            },
            "dt": 1773556842,
            "sys": {
                "type": 1,
                "id": 9308,
                "country": "VN",
                "sunrise": 1773529539,
                "sunset": 1773572745
            },
            "timezone": 25200,
            "id": 1561096,
            "name": "Xom Pho",
            "cod": 200
        }

        forecast_data = {
            "cod": "200",
            "message": 0,
            "cnt": 40,
            "list": [
                {
                "dt": 1773565200,
                "main": {
                    "temp": 24.49,
                    "feels_like": 24.77,
                    "temp_min": 24.49,
                    "temp_max": 25.52,
                    "pressure": 1017,
                    "sea_level": 1017,
                    "grnd_level": 1014,
                    "humidity": 68,
                    "temp_kf": -1.03
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 96
                },
                "wind": {
                    "speed": 5.08,
                    "deg": 135,
                    "gust": 5.57
                },
                "visibility": 10000,
                "pop": 1,
                "rain": {
                    "3h": 0.8
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-15 09:00:00"
                },
                {
                "dt": 1773576000,
                "main": {
                    "temp": 22.85,
                    "feels_like": 23.02,
                    "temp_min": 22.29,
                    "temp_max": 22.85,
                    "pressure": 1017,
                    "sea_level": 1017,
                    "grnd_level": 1015,
                    "humidity": 70,
                    "temp_kf": 0.56
                },
                "weather": [
                    {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 89
                },
                "wind": {
                    "speed": 4.76,
                    "deg": 129,
                    "gust": 8.16
                },
                "visibility": 10000,
                "pop": 0.79,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-15 12:00:00"
                },
                {
                "dt": 1773586800,
                "main": {
                    "temp": 20.72,
                    "feels_like": 20.96,
                    "temp_min": 20.72,
                    "temp_max": 20.72,
                    "pressure": 1018,
                    "sea_level": 1018,
                    "grnd_level": 1017,
                    "humidity": 81,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 21
                },
                "wind": {
                    "speed": 4.17,
                    "deg": 145,
                    "gust": 8.97
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-15 15:00:00"
                },
                {
                "dt": 1773597600,
                "main": {
                    "temp": 19.94,
                    "feels_like": 20.26,
                    "temp_min": 19.94,
                    "temp_max": 19.94,
                    "pressure": 1016,
                    "sea_level": 1016,
                    "grnd_level": 1016,
                    "humidity": 87,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 15
                },
                "wind": {
                    "speed": 3.45,
                    "deg": 131,
                    "gust": 7.65
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-15 18:00:00"
                },
                {
                "dt": 1773608400,
                "main": {
                    "temp": 19.91,
                    "feels_like": 20.23,
                    "temp_min": 19.91,
                    "temp_max": 19.91,
                    "pressure": 1015,
                    "sea_level": 1015,
                    "grnd_level": 1014,
                    "humidity": 87,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 94
                },
                "wind": {
                    "speed": 3.26,
                    "deg": 131,
                    "gust": 7.33
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-15 21:00:00"
                },
                {
                "dt": 1773619200,
                "main": {
                    "temp": 19.99,
                    "feels_like": 20.26,
                    "temp_min": 19.99,
                    "temp_max": 19.99,
                    "pressure": 1017,
                    "sea_level": 1017,
                    "grnd_level": 1016,
                    "humidity": 85,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 68
                },
                "wind": {
                    "speed": 3.3,
                    "deg": 134,
                    "gust": 6.98
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-16 00:00:00"
                },
                {
                "dt": 1773630000,
                "main": {
                    "temp": 21.29,
                    "feels_like": 21.56,
                    "temp_min": 21.29,
                    "temp_max": 21.29,
                    "pressure": 1018,
                    "sea_level": 1018,
                    "grnd_level": 1017,
                    "humidity": 80,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 87
                },
                "wind": {
                    "speed": 3.74,
                    "deg": 124,
                    "gust": 5.5
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.14
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-16 03:00:00"
                },
                {
                "dt": 1773640800,
                "main": {
                    "temp": 26.19,
                    "feels_like": 26.19,
                    "temp_min": 26.19,
                    "temp_max": 26.19,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 1013,
                    "humidity": 58,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 94
                },
                "wind": {
                    "speed": 4.23,
                    "deg": 164,
                    "gust": 5.75
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.16
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-16 06:00:00"
                },
                {
                "dt": 1773651600,
                "main": {
                    "temp": 26.74,
                    "feels_like": 27.46,
                    "temp_min": 26.74,
                    "temp_max": 26.74,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1010,
                    "humidity": 55,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 92
                },
                "wind": {
                    "speed": 5.54,
                    "deg": 160,
                    "gust": 6.72
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.2
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-16 09:00:00"
                },
                {
                "dt": 1773662400,
                "main": {
                    "temp": 23,
                    "feels_like": 23.21,
                    "temp_min": 23,
                    "temp_max": 23,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1012,
                    "humidity": 71,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 86
                },
                "wind": {
                    "speed": 6.54,
                    "deg": 155,
                    "gust": 11.07
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-16 12:00:00"
                },
                {
                "dt": 1773673200,
                "main": {
                    "temp": 21.29,
                    "feels_like": 21.69,
                    "temp_min": 21.29,
                    "temp_max": 21.29,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 1014,
                    "humidity": 85,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 19
                },
                "wind": {
                    "speed": 5.82,
                    "deg": 157,
                    "gust": 12.15
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-16 15:00:00"
                },
                {
                "dt": 1773684000,
                "main": {
                    "temp": 20.31,
                    "feels_like": 20.72,
                    "temp_min": 20.31,
                    "temp_max": 20.31,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 1013,
                    "humidity": 89,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 13
                },
                "wind": {
                    "speed": 3.74,
                    "deg": 144,
                    "gust": 9.66
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-16 18:00:00"
                },
                {
                "dt": 1773694800,
                "main": {
                    "temp": 19.48,
                    "feels_like": 19.94,
                    "temp_min": 19.48,
                    "temp_max": 19.48,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1012,
                    "humidity": 94,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 6
                },
                "wind": {
                    "speed": 2.88,
                    "deg": 140,
                    "gust": 8.22
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-16 21:00:00"
                },
                {
                "dt": 1773705600,
                "main": {
                    "temp": 20.01,
                    "feels_like": 20.39,
                    "temp_min": 20.01,
                    "temp_max": 20.01,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 1014,
                    "humidity": 89,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 13
                },
                "wind": {
                    "speed": 3.34,
                    "deg": 136,
                    "gust": 7.76
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.14
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-17 00:00:00"
                },
                {
                "dt": 1773716400,
                "main": {
                    "temp": 26.37,
                    "feels_like": 26.37,
                    "temp_min": 26.37,
                    "temp_max": 26.37,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 1014,
                    "humidity": 55,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                    }
                ],
                "clouds": {
                    "all": 26
                },
                "wind": {
                    "speed": 6.18,
                    "deg": 171,
                    "gust": 8.04
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-17 03:00:00"
                },
                {
                "dt": 1773727200,
                "main": {
                    "temp": 27.53,
                    "feels_like": 28.18,
                    "temp_min": 27.53,
                    "temp_max": 27.53,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1010,
                    "humidity": 53,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 60
                },
                "wind": {
                    "speed": 6.1,
                    "deg": 164,
                    "gust": 7.07
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-17 06:00:00"
                },
                {
                "dt": 1773738000,
                "main": {
                    "temp": 27.02,
                    "feels_like": 27.76,
                    "temp_min": 27.02,
                    "temp_max": 27.02,
                    "pressure": 1009,
                    "sea_level": 1009,
                    "grnd_level": 1009,
                    "humidity": 55,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 85
                },
                "wind": {
                    "speed": 6.62,
                    "deg": 149,
                    "gust": 7.25
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-17 09:00:00"
                },
                {
                "dt": 1773748800,
                "main": {
                    "temp": 23.22,
                    "feels_like": 23.43,
                    "temp_min": 23.22,
                    "temp_max": 23.22,
                    "pressure": 1012,
                    "sea_level": 1012,
                    "grnd_level": 1011,
                    "humidity": 70,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 54
                },
                "wind": {
                    "speed": 5.97,
                    "deg": 150,
                    "gust": 10.35
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-17 12:00:00"
                },
                {
                "dt": 1773759600,
                "main": {
                    "temp": 21.57,
                    "feels_like": 21.98,
                    "temp_min": 21.57,
                    "temp_max": 21.57,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1013,
                    "humidity": 84,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 4
                },
                "wind": {
                    "speed": 4.65,
                    "deg": 150,
                    "gust": 10.58
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-17 15:00:00"
                },
                {
                "dt": 1773770400,
                "main": {
                    "temp": 20.67,
                    "feels_like": 21.17,
                    "temp_min": 20.67,
                    "temp_max": 20.67,
                    "pressure": 1012,
                    "sea_level": 1012,
                    "grnd_level": 1011,
                    "humidity": 91,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 7
                },
                "wind": {
                    "speed": 3.14,
                    "deg": 132,
                    "gust": 7.18
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-17 18:00:00"
                },
                {
                "dt": 1773781200,
                "main": {
                    "temp": 19.87,
                    "feels_like": 20.42,
                    "temp_min": 19.87,
                    "temp_max": 19.87,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1011,
                    "humidity": 96,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 14
                },
                "wind": {
                    "speed": 2.64,
                    "deg": 126,
                    "gust": 5.94
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-17 21:00:00"
                },
                {
                "dt": 1773792000,
                "main": {
                    "temp": 20.55,
                    "feels_like": 21.06,
                    "temp_min": 20.55,
                    "temp_max": 20.55,
                    "pressure": 1014,
                    "sea_level": 1014,
                    "grnd_level": 1013,
                    "humidity": 92,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                    }
                ],
                "clouds": {
                    "all": 26
                },
                "wind": {
                    "speed": 2.45,
                    "deg": 136,
                    "gust": 4.68
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-18 00:00:00"
                },
                {
                "dt": 1773802800,
                "main": {
                    "temp": 26.04,
                    "feels_like": 26.04,
                    "temp_min": 26.04,
                    "temp_max": 26.04,
                    "pressure": 1015,
                    "sea_level": 1015,
                    "grnd_level": 1014,
                    "humidity": 62,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 61
                },
                "wind": {
                    "speed": 4.36,
                    "deg": 171,
                    "gust": 5.94
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.12
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-18 03:00:00"
                },
                {
                "dt": 1773813600,
                "main": {
                    "temp": 25.87,
                    "feels_like": 26.13,
                    "temp_min": 25.87,
                    "temp_max": 25.87,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1012,
                    "humidity": 62,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 81
                },
                "wind": {
                    "speed": 4.01,
                    "deg": 172,
                    "gust": 5.32
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-18 06:00:00"
                },
                {
                "dt": 1773824400,
                "main": {
                    "temp": 27.37,
                    "feels_like": 28.31,
                    "temp_min": 27.37,
                    "temp_max": 27.37,
                    "pressure": 1010,
                    "sea_level": 1010,
                    "grnd_level": 1009,
                    "humidity": 57,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 79
                },
                "wind": {
                    "speed": 4.28,
                    "deg": 152,
                    "gust": 4.9
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-18 09:00:00"
                },
                {
                "dt": 1773835200,
                "main": {
                    "temp": 23.68,
                    "feels_like": 24.01,
                    "temp_min": 23.68,
                    "temp_max": 23.68,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1011,
                    "humidity": 73,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04n"
                    }
                ],
                "clouds": {
                    "all": 75
                },
                "wind": {
                    "speed": 4.72,
                    "deg": 138,
                    "gust": 8.74
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-18 12:00:00"
                },
                {
                "dt": 1773846000,
                "main": {
                    "temp": 21.94,
                    "feels_like": 22.38,
                    "temp_min": 21.94,
                    "temp_max": 21.94,
                    "pressure": 1012,
                    "sea_level": 1012,
                    "grnd_level": 1011,
                    "humidity": 84,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                    }
                ],
                "clouds": {
                    "all": 44
                },
                "wind": {
                    "speed": 5.22,
                    "deg": 142,
                    "gust": 10.9
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-18 15:00:00"
                },
                {
                "dt": 1773856800,
                "main": {
                    "temp": 21.17,
                    "feels_like": 21.72,
                    "temp_min": 21.17,
                    "temp_max": 21.17,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1010,
                    "humidity": 91,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                    }
                ],
                "clouds": {
                    "all": 47
                },
                "wind": {
                    "speed": 4.05,
                    "deg": 126,
                    "gust": 9.18
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-18 18:00:00"
                },
                {
                "dt": 1773867600,
                "main": {
                    "temp": 20.47,
                    "feels_like": 21.08,
                    "temp_min": 20.47,
                    "temp_max": 20.47,
                    "pressure": 1010,
                    "sea_level": 1010,
                    "grnd_level": 1009,
                    "humidity": 96,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                    }
                ],
                "clouds": {
                    "all": 46
                },
                "wind": {
                    "speed": 3.11,
                    "deg": 117,
                    "gust": 7.11
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-18 21:00:00"
                },
                {
                "dt": 1773878400,
                "main": {
                    "temp": 21.07,
                    "feels_like": 21.66,
                    "temp_min": 21.07,
                    "temp_max": 21.07,
                    "pressure": 1012,
                    "sea_level": 1012,
                    "grnd_level": 1011,
                    "humidity": 93,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 54
                },
                "wind": {
                    "speed": 2.91,
                    "deg": 130,
                    "gust": 6.26
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-19 00:00:00"
                },
                {
                "dt": 1773889200,
                "main": {
                    "temp": 25.14,
                    "feels_like": 25.51,
                    "temp_min": 25.14,
                    "temp_max": 25.14,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1012,
                    "humidity": 69,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 80
                },
                "wind": {
                    "speed": 4.15,
                    "deg": 170,
                    "gust": 5.52
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.1
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-19 03:00:00"
                },
                {
                "dt": 1773900000,
                "main": {
                    "temp": 28.39,
                    "feels_like": 29.79,
                    "temp_min": 28.39,
                    "temp_max": 28.39,
                    "pressure": 1009,
                    "sea_level": 1009,
                    "grnd_level": 1008,
                    "humidity": 58,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                    }
                ],
                "clouds": {
                    "all": 89
                },
                "wind": {
                    "speed": 3.8,
                    "deg": 198,
                    "gust": 6.12
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-19 06:00:00"
                },
                {
                "dt": 1773910800,
                "main": {
                    "temp": 30.82,
                    "feels_like": 31.78,
                    "temp_min": 30.82,
                    "temp_max": 30.82,
                    "pressure": 1006,
                    "sea_level": 1006,
                    "grnd_level": 1005,
                    "humidity": 47,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01d"
                    }
                ],
                "clouds": {
                    "all": 4
                },
                "wind": {
                    "speed": 6.73,
                    "deg": 154,
                    "gust": 6.56
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-19 09:00:00"
                },
                {
                "dt": 1773921600,
                "main": {
                    "temp": 24.89,
                    "feels_like": 25.31,
                    "temp_min": 24.89,
                    "temp_max": 24.89,
                    "pressure": 1008,
                    "sea_level": 1008,
                    "grnd_level": 1008,
                    "humidity": 72,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 2
                },
                "wind": {
                    "speed": 6.18,
                    "deg": 147,
                    "gust": 9.96
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-19 12:00:00"
                },
                {
                "dt": 1773932400,
                "main": {
                    "temp": 23.01,
                    "feels_like": 23.64,
                    "temp_min": 23.01,
                    "temp_max": 23.01,
                    "pressure": 1010,
                    "sea_level": 1010,
                    "grnd_level": 1009,
                    "humidity": 87,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 800,
                    "main": "Clear",
                    "description": "clear sky",
                    "icon": "01n"
                    }
                ],
                "clouds": {
                    "all": 6
                },
                "wind": {
                    "speed": 5.03,
                    "deg": 144,
                    "gust": 10.51
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-19 15:00:00"
                },
                {
                "dt": 1773943200,
                "main": {
                    "temp": 22.3,
                    "feels_like": 22.91,
                    "temp_min": 22.3,
                    "temp_max": 22.3,
                    "pressure": 1009,
                    "sea_level": 1009,
                    "grnd_level": 1008,
                    "humidity": 89,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03n"
                    }
                ],
                "clouds": {
                    "all": 35
                },
                "wind": {
                    "speed": 4.04,
                    "deg": 128,
                    "gust": 9.23
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-19 18:00:00"
                },
                {
                "dt": 1773954000,
                "main": {
                    "temp": 22.12,
                    "feels_like": 22.71,
                    "temp_min": 22.12,
                    "temp_max": 22.12,
                    "pressure": 1008,
                    "sea_level": 1008,
                    "grnd_level": 1008,
                    "humidity": 89,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10n"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 3.7,
                    "deg": 121,
                    "gust": 8
                },
                "visibility": 10000,
                "pop": 0.2,
                "rain": {
                    "3h": 0.15
                },
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2026-03-19 21:00:00"
                },
                {
                "dt": 1773964800,
                "main": {
                    "temp": 22,
                    "feels_like": 22.61,
                    "temp_min": 22,
                    "temp_max": 22,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1010,
                    "humidity": 90,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 3.18,
                    "deg": 105,
                    "gust": 5.77
                },
                "visibility": 10000,
                "pop": 0.25,
                "rain": {
                    "3h": 0.38
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-20 00:00:00"
                },
                {
                "dt": 1773975600,
                "main": {
                    "temp": 23.48,
                    "feels_like": 24.08,
                    "temp_min": 23.48,
                    "temp_max": 23.48,
                    "pressure": 1013,
                    "sea_level": 1013,
                    "grnd_level": 1012,
                    "humidity": 84,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 3,
                    "deg": 117,
                    "gust": 4.41
                },
                "visibility": 10000,
                "pop": 0.51,
                "rain": {
                    "3h": 0.3
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-20 03:00:00"
                },
                {
                "dt": 1773986400,
                "main": {
                    "temp": 23.68,
                    "feels_like": 24.4,
                    "temp_min": 23.68,
                    "temp_max": 23.68,
                    "pressure": 1011,
                    "sea_level": 1011,
                    "grnd_level": 1010,
                    "humidity": 88,
                    "temp_kf": 0
                },
                "weather": [
                    {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                    }
                ],
                "clouds": {
                    "all": 100
                },
                "wind": {
                    "speed": 2.84,
                    "deg": 112,
                    "gust": 4.38
                },
                "visibility": 10000,
                "pop": 1,
                "rain": {
                    "3h": 1.38
                },
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2026-03-20 06:00:00"
                }
            ],
            "city": {
                "id": 1561096,
                "name": "Xom Pho",
                "coord": {
                "lat": 21.0294,
                "lon": 105.8544
                },
                "country": "VN",
                "population": 2000,
                "timezone": 25200,
                "sunrise": 1773529539,
                "sunset": 1773572745
            }
            }

        return {
            "current": current_data,
            "forecast": forecast_data
        }
