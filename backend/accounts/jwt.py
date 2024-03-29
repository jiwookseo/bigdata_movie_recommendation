import requests
import json
import os

NODE_ENV = os.environ.get("NODE_ENV", "develop")
BASE_URL = "http://52.78.81.59:8000/api/token/" if NODE_ENV == "production" else "http://localhost:8000/api/token/"
headers = {'content-type': 'application/json'}


def create_token(user):
    return requests.post(BASE_URL + "create/", data=json.dumps(user), headers=headers)


def verify_token(token):
    return requests.post(BASE_URL + "verify/", data=json.dumps({"token": token}), headers=headers)


def refresh_token(token):
    return requests.post(BASE_URL + "refresh/", data=json.dumps({"token": token}), headers=headers)
