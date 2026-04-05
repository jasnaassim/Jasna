import datetime
from tkinter import *
import requests
import smtplib
import time

my_email = "jasnaassim2@gmail.com"
my_password = "vhnm cuxk kjsr gtvx"

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def iss_overhead():
    iss_latitude = float(data["iss-position"]["latitude"])
    iss_longitude = float(data["iss-position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "date": "today"
    }
    response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() or is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Sub: Look Up\nThe ISS is above you"
        )
