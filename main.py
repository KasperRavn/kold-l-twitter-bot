import requests
import tweepy
import os
from dotenv import load_dotenv
import random

billeder_varm_dag = [
    "billedervarm/4c6659fd41a3f40da8e9a4f6b8b845aa.jpg",
    "billedervarm/114081_CB-Content-Stills-11.1_0001.jpg",
    "billedervarm/Another.jpg",
    "billedervarm/DjrcwhwWsAAo6in.jpg",
    "billedervarm/ED00.jpg",
    "billedervarm/mads_snap.jpg",
    "billedervarm/Mads-20181008044152493.jpg",
    "billedervarm/mads-mikkelsen-carlsberg-00-1.jpg",
    "billedervarm/mads-mikkelsen-carlsberg-00-3.jpg",
    "billedervarm/Skærmbillede-2020-10-12-kl.-21.57.51.png"
]

billeder_kold_dag = [
    "billederkold/1d574add22a25762e9016a4417d66f9c.jpg",
    "billederkold/70lek7.png",
    "billederkold/mads-mikkelsen-sad.png",
    "billederkold/the-hunt-mads-mikkelsen-cry.avif",
    "billederkold/unnamed.jpg"
]

tilfældigt_tal_varm = random.randint(0,9)
tilfældigt_tal_kold = random.randint(0,4)


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




client = tweepy.Client(bearer_token, consumer_key, consumer_key_secret, access_token, access_token_secret, wait_on_rate_limit=True)

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)




BASE_DIR = os.path.dirname(__file__)
fil_varm = os.path.join(BASE_DIR, billeder_varm_dag[tilfældigt_tal_varm])
fil_kold = os.path.join(BASE_DIR, billeder_kold_dag[tilfældigt_tal_kold])



def lav_tweet(temp_klokken_tolv):
    if temp_klokken_tolv > 15:
        media_id_varm = api.media_upload(filename=fil_varm).media_id_string
        client.create_tweet(text="Ja i dag er en farlig dag at være en kold øl på", media_ids=[media_id_varm])
    else:
        media_id_kold = api.media_upload(filename=fil_kold).media_id_string
        client.create_tweet(text="Nej i dag er ikke en farlig dag at være en kold øl på", media_ids=[media_id_kold])


lav_tweet(temp_klokken_tolv)
