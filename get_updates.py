import requests
import os

TOKEN = os.environ["TOKEN"]
BASE_URL = os.environ["BASE_URL"]

def get_updates() -> dict:
    '''getting info about the bot'''
    url = f"{BASE_URL}{TOKEN}/getUpdates"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result'] 
    
    return False