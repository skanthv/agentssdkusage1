
from agents import function_tool

from dotenv import load_dotenv
load_dotenv()
import os

import requests

@function_tool
def get_weather(location: str) -> str:
    weatherapi_key = os.getenv("WEATHER_API_KEY")

    if weatherapi_key:
        url = "https://api.weatherapi.com/v1/current.json"
        params = {"key": weatherapi_key, "q": location, "aqi": "no"}
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        name = data.get("location", {}).get("name", location)
        country = data.get("location", {}).get("country", "")
        cur = data.get("current", {}) or {}
        temp_c = cur.get("temp_c")
        cond = (cur.get("condition") or {}).get("text", "")
        return f"{name}{', ' + country if country else ''}: {temp_c}°C, {cond}"
    else:
        return "Weather API key not found."

#print(get_weather("New York"))