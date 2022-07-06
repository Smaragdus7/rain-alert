import requests
import smtplib
import os

MY_EMAIL = "@gmail.com"
MY_PASS = ""

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = 23.72252721946793
MY_LON = -103.5836949363556

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "alerts,minutely",
    "units": "metric",
    "lang": "es",
    "appid": API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

hourly_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in hourly_slice:
    code = hour_data["weather"][0]["id"]
    if code < 805:
        will_rain = True
if will_rain:
    print("Lleva una sombrilla ☂")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: Lleva una sombrilla ☂\n\nSe pronostica lluvia las próximas 12 horas."
    )
