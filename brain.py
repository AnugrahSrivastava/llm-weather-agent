import json
from config import client, MODEL_NAME

def narrate_weather(city, weather_data):

    prompt = f"""
You are a weather assistant.

Convert this weather data into a short, friendly summary.

City: {city}

Data:
Temperature: {weather_data['temperature']} C
Wind Speed: {weather_data['wind']} km/h
Conditions: {weather_data['conditions']}

Rules:
- 1–2 sentences
- Natural tone
- No extra facts
- Do not invent anything
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You summarize weather data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

def decide_action(city: str) -> dict:
    response = client.chat.completions.create(
        model= MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an AI agent."},
            {
                "role": "user",
                "content": f"""
User wants the weather.

City: {city}

Respond ONLY in JSON:
{{
  "thought": "...",
  "action": "get_weather"
}}
"""
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "thought": "Model returned invalid JSON",
            "action": "error"
        }