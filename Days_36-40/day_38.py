# Day 38 of 100 Days of Code Challenge
# Google Sheets workout tracker

import requests
import os
from datetime import datetime

# nutritionix api
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# sheety api
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
sheety_header = {
    "Authorization": SHEETY_TOKEN,
    "Content-Type": "application/json"
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/86606403943ba68730bf95a2c5eac4c3/myWorkouts/workouts"

# pull user workout data from nutritionix api
workout = input("Tell me what exercises you did: ")

exercise_params = {
    "query": workout,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 175,
    "age": 24
}

response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
data = response.json()

# add exercise info to google sheet spreadsheet
for ex in data["exercises"]:
    log_config = {
        "workout": {
            "date": datetime.now().strftime('%d/%m/%Y'),
            "time": datetime.now().strftime('%I:%M%p'),
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"],
        }
    }

    r = requests.post(url=sheety_endpoint, json=log_config, headers=sheety_header)
    print(r.text)
