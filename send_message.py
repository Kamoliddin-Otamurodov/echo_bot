import requests
import os

TOKEN = os.environ["TOKEN"]
BASE_URL = os.environ["BASE_URL"]

def send_message(chat_id: str, text: str) -> None:
    '''sending messages'''
    url = f"{BASE_URL}{TOKEN}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': f"*{text}*",
        'parse_mode': "MarkdownV2"
    }

    response = requests.get(url=url, params=payload)

    return response.status_code