import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 429:
    print("Too many requests. Waiting before retrying...")
    time.sleep(10)
elif response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)

# We should not print the city name because location is personal data.
# As per privacy rules , we should avoid exposing user data unless necessary.