import requests
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 163
HEIGHT_CM = 160
AGE = 37

APP_ID = "app_be6b36caa36a419da6fb9945"
API_KEY = "nix_live_n8bScN6k8IasiZuVPnaZereDSOvyQ1fY"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

sheety_url = "https://api.sheety.co/e7c3f5ca48a7066563018c2d952e13ec/myWorkouts/workouts"

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs)

    print(sheet_response.text)
