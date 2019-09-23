# Python
import requests
import json


# Variables
API_URL = 'http://localhost:8000/cluster/'
headers = {'content-type': 'application/json'}


def recm_movies(method):
    requests.post(API_URL + "users/recm_movies/{}/".format(method), headers=headers)



if __name__ == '__main__':
    print("Movie-Based KNN 진행 중")
    recm_movies('mb')
    print("Movie-Based KNN 완료")
    print("User-Based KNN 진행 중")
    recm_movies('ub')
    print("User-Based KNN 완료")

    print('KNN-Based를 통한 추천 영화 정보가 모두 데이터베이스에 저장되었습니다.')