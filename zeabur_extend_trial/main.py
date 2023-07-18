import os

import requests
from dotenv import load_dotenv

load_dotenv()


def checkin() -> str:
    url = 'https://gateway.zeabur.com/graphql'
    token = os.getenv('ZEABUR_API_TOKEN')
    print(f'token:{token}\n')
    body = {
        "operationName": "CheckIn",
        "variables": {},
        "query": "mutation CheckIn {\n  checkIn\n}",
    }
    headers = {"authorization": f"Bearer {token}"}
    resp = requests.post(url, json=body, headers=headers)
    print(resp.json())
    return resp.json()
