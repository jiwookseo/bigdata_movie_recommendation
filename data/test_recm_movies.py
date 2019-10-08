# Python
import requests
import json
import pprint


API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

# 사용자 별 맞춤 추천 영화 API 테스트 코드
def recm_movies_test():
    response = requests.get(API_URL + "users/{}/recm_movies/".format("user1"), headers=headers)
    pprint.pprint(response.text)

if __name__ == '__main__':
    recm_movies_test()