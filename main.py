from brain import decide_action, narrate_weather
from tools import get_weather
from memory import get_last_city, save_last_city

def resolve_city(user_input):
    if user_input.lower() == "same":
        last = get_last_city()
        if last:
            print(f"Using last city: {last}")
            return last
        else:
            print("No previously stored city found.")   
            return None
    return user_input

def run_agent():
    raw = input("Enter city name (or 'same' for last city): ")

    city = resolve_city(raw)

    if not city:
        return
    

    print("\nThinking...")
    decision = decide_action(city)

    print("Thought:", decision.get("thought"))

    if decision.get("action") == "get_weather":
       summary = narrate_weather(city, get_weather(city))
       print("\n🗣 Weather Summary:")
       print(summary)
       save_last_city(city)
    else:
        print("\nAgent could not decide an action.")

if __name__ == "__main__":
    run_agent()