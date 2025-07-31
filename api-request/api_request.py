import requests 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('api_key')
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"
def fetch_data():
    print("Fetching weather data from the weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        print("API response received successfully.")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
  
fetch_data()


def mock_fetch_data():
    print("Mocking the API response for testing purposes.")
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-07-28 13:32', 'localtime_epoch': 1753709520, 'utc_offset': '-4.0'}, 'current': {'observation_time': '05:32 PM', 'temperature': 33, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '05:49 AM', 'sunset': '08:15 PM', 'moonrise': '09:50 AM', 'moonset': '10:19 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 11}, 'air_quality': {'co': '501.35', 'no2': '12.95', 'o3': '158', 'so2': '5.92', 'pm2_5': '27.38', 'pm10': '28.305', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 4, 'wind_degree': 257, 'wind_dir': 'WSW', 'pressure': 1016, 'precip': 0, 'humidity': 43, 'cloudcover': 25, 'feelslike': 37, 'uv_index': 9, 'visibility': 16, 'is_day': 'yes'}}