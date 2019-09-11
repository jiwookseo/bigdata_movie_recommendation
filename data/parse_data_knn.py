# Python
import requests
import json


# Variables
API_URL = 'http://localhost:8000/cluster/'
headers = {'content-type': 'application/json'}


def recm_movies(method):
    requests.post(API_URL + "users/recm_movies/{}/".format(method), headers=headers)



if __name__ == '__main__':
    recm_movies('mb')

    print('FINISH')