import requests

API_KEY = "3157c0eafa154fab8c8194316261606"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(location):
    url = f"{BASE_URL}?key={API_KEY}&q={location}&aqi=yes"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print("Error:", data["error"]["message"])
            return

        city = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        aqi = data["current"]["air_quality"]["pm2_5"]

        print("\n--- Weather Report ---")
        print(f"Location: {city}, {country}")
        print(f"Temperature: {temp_c}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_kph} kph")
        print(f"Air Quality PM2.5: {aqi:.2f}")

    except Exception as e:
        print("Something went wrong:", e)


location = input("Enter your city name: ")
get_weather(location)