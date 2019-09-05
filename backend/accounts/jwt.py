import requests, json

BASE_URL = "http://localhost:8000/api/token/"
headers = {'content-type': 'application/json'}


def create_token(user):
    return requests.post(BASE_URL + "create/", data=json.dumps(user), headers=headers)


def verify_token(token):
    return requests.post(BASE_URL + "verify/", data=json.dumps({"token": token}), headers=headers)


def refresh_token(token):
    return requests.post(BASE_URL + "refresh/", data=json.dumps({"token": token}), headers=headers)
