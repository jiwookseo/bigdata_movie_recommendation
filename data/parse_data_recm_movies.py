# Python
import requests
import json



# Variables
API_URL = 'http://localhost:8000/cluster/'
headers = {'content-type': 'application/json'}


def recommended_movies(method):
    requests.post(API_URL + "users/recommended_movies/{}/".format(method), headers=headers)



if __name__ == '__main__':
    # print("Movie-Based KNN 진행 중")
    # recommended_movies('mb')
    # print("Movie-Based KNN 완료")

    # print("User-Based KNN 진행 중")
    # recommended_movies('ub')
    # print("User-Based KNN 완료")

    print("Matrix Factorization 진행 중")
    recommended_movies('mf')
    print("Matrix Factorization 완료")

    print('사용자 별 맞춤 추천 영화 정보가 모두 데이터베이스에 저장되었습니다.')