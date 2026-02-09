import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except json.JSONDecodeError:
        # Corrupted or invalid JSON
        return {}


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def save_last_city(city):
    memory = load_memory()
    memory["last_city"] = city
    save_memory(memory)       

def get_last_city():
    memory = load_memory()
    return memory.get("last_city")