import requests
import tweepy
import os
from dotenv import load_dotenv


BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=55.6759&longitude=12.5655&hourly=temperature_2m&timezone=auto"

url = BASE_URL

response = requests.get(url).json()
temp_klokken_tolv = response['hourly']['temperature_2m'][12]

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_key_secret = os.getenv("CONSUMER_KEY_SECRET")


client = tweepy.Client(bearer_token, consumer_key, consumer_key_secret, access_token, access_token_secret)

def lav_tweet(temp_klokken_tolv):
    if temp_klokken_tolv > 15:
        client.create_tweet(text="xdd")
    else:
        client.create_tweet(text="Nej i dag er ikke en farlig dag at være en kold øl på")


lav_tweet(temp_klokken_tolv)