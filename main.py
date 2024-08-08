import requests
import time
from get_updates import get_updates
from send_message import send_message
import os

TOKEN = os.environ["TOKEN"]
BASE_URL = os.environ["BASE_URL"]

def echo():
    update_id = 0

    while True:
        time.sleep(0.5)

        # print(f'updates: {update_id}')
        updates = get_updates()
        if updates[-1]['update_id'] == update_id:
            continue
        else:
            last_update = updates[-1]
            
            message = last_update['message']
            # pprint(message)
            print(message["text"])

            chat_id = message['chat']['id']

            if 'text' in message.keys():
                text = message['text']
                send_message(chat_id, text)

        update_id = updates[-1]['update_id']

echo()