# Day 33 of 100 Days of Code Challenge
# ISS Tacker

import requests
from datetime import datetime
import pytz
import smtplib
import time

MY_LAT = 44.859741
MY_LONG = -91.696251
USER = "pythonbot97@gmail.com" # created to test code
PASS = "password" # dummy password

# Retrieve ISS position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_data = response.json()
longitude = float(iss_data["iss_position"]["longitude"])
latitude = float(iss_data["iss_position"]["latitude"])

iss_position = latitude, longitude

# Retrieving sunrise and sunset times to ensure it's dark outside to be able to see the ISS
now = datetime.now()
now_utc = now.astimezone(pytz.utc)  # sunset-sunrise api returns time in utc

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_hour = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split('T')[1].split(":")[0])

# Boolean variables to store if it's dark out and if the ISS is near
is_dark = now_utc.hour >= sunset_hour or now_utc.hour <= sunrise_hour
is_iss_near = (MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5) \
              and (MY_LONG - 5 <= iss_position[1] <= MY_LONG + 5)

# Send an email every 60 seconds when the ISS is near
if is_dark and is_iss_near:
    while is_iss_near:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASS)
            connection.sendmail(
                from_addr=USER,
                to_addrs=USER,
                msg=f"Subject:Look Up!\n\nThe ISS is above you.")
        time.sleep(60)
