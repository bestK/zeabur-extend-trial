import os

import requests
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


def checkin() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    token_str = os.getenv('ZEABUR_API_TOKEN')
    if token_str is None:
        print(f'{now} token must not be none!')
        return

    tokens = token_str.split(",")    

    url = 'https://gateway.zeabur.com/graphql'
    
    body = {
        "operationName": "CheckIn",
        "variables": {},
        "query": "mutation CheckIn {\n  checkIn\n}",
    }
    
    for token in tokens:
        headers = {"authorization": f"Bearer {token}"}
        resp = requests.post(url, json=body, headers=headers)
        output = f'{now} {token[:15] + "..."} {resp.json()}'
        print(output)


if __name__ == "__main__":
    checkin()
