import os

import requests
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


def checkin() -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    token = os.getenv('ZEABUR_API_TOKEN')
    if token is None:
        print(f'{now} token must not be none!')
        return

    url = 'https://gateway.zeabur.com/graphql'
    
    body = {
        "operationName": "CheckIn",
        "variables": {},
        "query": "mutation CheckIn {\n  checkIn\n}",
    }
    headers = {"authorization": f"Bearer {token}"}
    resp = requests.post(url, json=body, headers=headers)
 
    
    output = f'{now} {token[:15] + "..."} {resp.json()}\n'
    print(output)

    return resp.json()

if __name__ == "__main__":
    checkin()
