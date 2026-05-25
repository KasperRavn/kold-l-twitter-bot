import requests
import tweepy
import os


BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=55.6759&longitude=12.5655&hourly=temperature_2m&timezone=auto"

url = BASE_URL

response = requests.get(url).json()
temp_klokken_tolv = response['hourly']['temperature_2m'][12]
temp_klokken_tolv_json = {"temperatur": temp_klokken_tolv}

print(temp_klokken_tolv_json)