import requests

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    95: "Thunderstorm"
}

def get_weather(city: str) -> str:
    geo_resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
        timeout=10
    )
    geo = geo_resp.json()

    if not geo.get("results"):
        return "City not found."

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    weather_resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        },
        timeout=10
    )

    weather_data = weather_resp.json()
    weather = weather_data.get("current_weather")

    if not weather:
        return "Weather data unavailable."

    code = weather.get("weathercode")
    description = WEATHER_CODES.get(code, "Unknown weather condition")

    return {
        "conditions": description,
        "temperature": weather['temperature'],
        "wind": weather['windspeed']
    }