
from dotenv import load_dotenv, find_dotenv
import os
import requests
import datetime

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

gender = "male"
weight_kg = 62.50
height_cm = 174.50
age = 22

app_id = os.environ.get("NUTRITION_APP_ID")
app_key = os.environ.get("NUTRITION_APP_KEY")
sheety_auth = os.environ.get("SHEETY_AUTH")
username = os.environ.get("SHEETY_USERNAME")

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key
}

host_domain = "https://trackapi.nutritionix.com"

app_params = {
    "query": input("Exercise: "),
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}



exercise_endpoint = f"{host_domain}/v2/natural/exercise"

response = requests.post(exercise_endpoint, json=app_params, headers=headers)
response.raise_for_status()

data = response.json()
exercise_data =  data["exercises"][0]

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%I:%M:%S %p")
exercise_name = exercise_data["user_input"].capitalize()
duration = f"{exercise_data["duration_min"]}"
calories = f"{exercise_data["nf_calories"]}"
print(time)

sheety_endpoint = f"https://api.sheety.co/{username}/myWorkouts/workouts"

sheety_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }
}

headers = {
    "Authorization": sheety_auth
}

sheety_response = requests.post(sheety_endpoint, json=sheety_params, headers=headers)
sheety_response.raise_for_status()




