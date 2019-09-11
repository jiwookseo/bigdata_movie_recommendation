# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie

# Variables and Functions For Data Processing : data_views.py
from .data_views import data_preprocessing, update_clustering_data, kmeans_custom_clustering_users
from .data_views import cos_sim

# Data Processing & Clustering Libs 
import numpy as np

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning



# User Clustering
@api_view(['POST'])
def user_clustering(request):
    users_data = data_preprocessing('u')
    print("data preprocessing is completed")
    method = request.data.get('method')
    k = request.data.get('k', 7)

    # K-Means
    if method == 'km':
        model = KMeans(n_clusters=k, init="random", random_state=0)
        model.fit(users_data)
        clustering_data = model.predict(users_data)

    # Hierarchy
    elif method == 'hr':
        model = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage='ward')
        clustering_data = model.fit_predict(users_data)

    # EM
    elif method == 'em':
        model = GaussianMixture(n_components=k, init_params='random', random_state=0, max_iter=100)
        with ignore_warnings(category=ConvergenceWarning):
            model.fit(users_data)
        clustering_data = model.predict(users_data)

    # K-Means Customized
    elif method == 'kmc':
        clustering_data = kmeans_custom_clustering_users(k, 100, users_data)

    else:
        print("method를 정확히 표기해주세요.")
        return Response(status=status.HTTP_400_BAD_REQUEST)

    print("clustering is completed")
    update_clustering_data('u', clustering_data)        
    print("to update clustering data is completed")
    
    return Response(status=status.HTTP_201_CREATED)



# Expected Ratings
# @api_view(['POST'])
# def expected_ratings(request, method):

#     # 인덱스 변수 정의
#     ml = Movie.objects.last().id
#     ul = User.objects.last().id

#     # 유사한 데이터의 수, K 정의
#     k = 10

#     # user-rating matrix인 users_data 생성
#     users_data = data_preprocessing('u')


#     # Movie Based
#     if method == 'mb':

#         # Step 1. 유사도 데이터 생성을 위한 movie-rating matrix 생성
#         movies_data = data_preprocessing('m')

#         # Step 2. 영화 유사도 데이터 생성
#         movie_similarity = np.zeros((ml, ml))

#         for i in range(ml):
#             for j in range(i+1, ml):  
#                 cosine_similarity = round(cos_sim(movies_data[i, :], movies_data[j, :]), 2)
#                 movie_similarity[i, j] = cosine_similarity
#                 movie_similarity[j, i] = cosine_similarity
                
#             print("영화 유사도 데이터 생성중... {}/{}".format(i, ml))          
#         print("영화 유사도 데이터 생성 완료")

#         # Step 3. 평점 계산 및 입력
#         # for i in range(ul):
#         #     for j in range(ml):
#         #         # user i+1 -> movie j+1

#         #         # User, Movie가 DB에 존재하는지 확인, 없으면 패스
#         #         # try:
#         #         #     user = User.objects.get(pk=i+1)
#         #         #     movie = Movie.objects.get(pk=j+1)
#         #         # except:
#         #         #     continue
                
#         #         # 만약 평점을 남겼다면, 예상평점을 구할 이유가 없으므로 패스, 
#         #         if users_data[i, j] > 0:
#         #             continue
                    
#         #         # j+1번째 영화와 유사한 영화 순으로 정렬, 평점을 위한 cnt와 total 변수 초기화
#         #         similar_movies = np.argsort(movie_similarity[j, :])[::-1]
#         #         total = 0
#         #         cnt = 0
                
#         #         for mv in similar_movies:         
#         #             if cnt > k:
#         #                 break
                        
#         #             # i+1의 유저가 해당 영화에 평점을 남겼다면?
#         #             if users_data[i, mv] > 0:
#         #                 total += users_data[i, mv]
#         #                 cnt += 1
                        
#         #         # 평점 구하기
#         #         if cnt == 0:
#         #             exp_rating = 0
#         #         else:
#         #             exp_rating = round((total / cnt), 2)
                    
#         #         # 구한 평점을 DB에 넣기
#         #         try:
#         #             exp_rating_record = ExpectedRating.objects.get(user=user, movie=movie)
#         #             exp_rating_record.ex_rating_mb = exp_rating
#         #             exp_rating_record.save()
#         #         except ExpectedRating.DoesNotExist:
#         #             exp_rating = ExpectedRating(user=user, movie=movie, ex_rating_mb=exp_rating)
#         #             exp_rating.save()
                
#             print("데이터를 계산 중입니다... {}/{}".format(i+1, ul))
#         print("예상 평점이 모두 DB에 저장되었습니다.")     


#     elif method == 'ub':
#         # 유저 유사도 데이터 생성
#         user_similarity = np.zeros((ul, ul))
#         # 평점 계산 및 입력
#         pass

#     else:
#         print("메소드를 정확히 입력해주세요.")