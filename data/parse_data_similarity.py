# Python
import requests
import json

# Data Processing Tools
import numpy as np
from numpy import dot
from numpy.linalg import norm


# Variables
API_URL = 'http://localhost:8000/cluster/'
headers = {'content-type': 'application/json'}


def movie_similarity():
    requests.post(API_URL + 'movie_similarity/', headers=headers)

def user_similarity():
    requests.post(API_URL + 'user_similarity/', headers=headers)



# Execution
if __name__ == '__main__':
    movie_similarity()
    # user_similarity()
    print('FINISH')