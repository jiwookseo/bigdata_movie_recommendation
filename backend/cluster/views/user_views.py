# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie
from cluster.models import RecommendedMovie

# Variables and Functions For Data Processing : data_views.py
# Used for Clustering, KNN, MF Algorithm
from .data_views import create_rating_matrix, update_clustering_data, kmeans_custom_clustering_users
from .data_views import cosine_similarity, create_similarity_matrix, create_recommended_movie
from .data_views import alternating_least_squares

# Data Processing & Clustering Libraries
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning



# User Clustering
# Algorithms : K-Means, Hierarchy, EM
@api_view(['POST'])
def user_clustering(request):
    users_data = create_rating_matrix('u')
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



# 사용자 별 맞춤 영화 데이터 생성
# Algorithms : KNN(Movie Based, User Based), MF
@api_view(['POST'])
def recommended_movies(request, method):
    
    # nm : 영화 수, number of movies
    # nu : 유저 수, number of users
    # K : 유사한 데이터를 의미하는 Neighbor의 수
    # R : 사용자 별 영화에 대한 평점 행렬, user-rating matrix
    # R_trans : 영화 별 사용자에 대한 평점 행렬, movie-rating matrix
    # R_pred : 사용자 별 영화에 대한 예상 평점(선호도) 행렬
    nm = Movie.objects.last().id
    nu = User.objects.last().id
    k = 10
    R = create_rating_matrix('u')

    # KNN - Movie Based
    if method == 'mb':    
        R_pred = np.copy(R)
        R_trans = create_rating_matrix('m')
        print("변수 및 데이터 생성 완료.")

        # 영화 유사도 데이터 생성
        movie_similarity_matrix = create_similarity_matrix(R_trans, nm)              
        print("영화 유사도 데이터 생성 완료")

        # 평점 계산 및 입력
        for i in range(nu):
            # User가 있을 경우 Movie에 대해 순회하며 예상 평점 계산 (user i+1 -> movie j+1)
            for j in range(nm):

                # 만약 평점을 남겼다면, 예상평점을 구할 이유가 없으므로 패스, 
                if R[i, j] > 0:
                    continue
                    
                # 현재 영화와 유사한 영화 순으로 정렬, 평점을 위한 cnt와 total 변수 초기화
                similar_movies = np.argsort(movie_similarity_matrix[j, :])[::-1]
                total = 0
                cnt = 1
                
                for mv in similar_movies:         
                    if cnt > k:
                        break
                        
                    # i+1의 유저가 해당 영화에 평점을 남겼다면 total과 cnt에 합산.
                    if R[i, mv] > 0:
                        total += R[i, mv]
                        cnt += 1
                        
                # 평점 구하기 (total / cnt)
                if cnt == 0:
                    exp_rating = 0
                else:
                    exp_rating = round((total / cnt), 2)

                # 구한 평점을 R_pred에 넣기
                R_pred[i, j] = exp_rating
            
            print("평점 계산 및 입력 중, {}/{}".format(i, nu))
        print("평점 계산 및 입력 완료")

                
    # KNN - User Based
    elif method == 'ub':
        R_pred = np.copy(R)
        print("변수 및 데이터 생성 완료.")

        # 사용자 유사도 데이터 생성
        user_similarity_matrix = create_similarity_matrix(R, nu)                
        print("사용자 유사도 데이터 생성 완료")   

        # 평점 계산 및 입력
        for i in range(nu):
            for j in range(nm):
                # user i+1 -> movie j+1
                
                # 만약 평점을 남겼다면, 예상평점을 구할 이유가 없으므로 패스, 
                if R[i, j] > 0:
                    continue
                
                # 유사한 유저들 순으로 정렬, 평점을 위한 cnt와 total 변수 초기화
                similar_users = np.argsort(user_similarity_matrix[i])[::-1]
                cnt = 0
                total = 0
                
                for user in similar_users:
                    # k명 까지만 계산에 포함한다.
                    if cnt > k:
                        break
                        
                    # 해당 유저가 평점을 남겼다면?
                    if R[user, j] > 0:
                        total += R[user, j]
                        cnt += 1
            
                # 평점 구하기 (total / cnt), division by zero 예외 처리
                if cnt == 0:
                    exp_rating = 0
                else:
                    exp_rating = round((total / cnt), 2)
                
                # 구한 평점을 R_pred에 넣기
                R_pred[i, j] = exp_rating

            print("평점 계산 및 입력 중, {}/{}".format(i, nu))
        print("평점 계산 및 입력 완료")


    # Matrix Factorization
    elif method == 'mf':
        # lmda = 정규화를 위한 람다
        # nf : 잠재 요인의 수, number of Latent Factors
        lmda = 1
        nf = 18

        # U : User Latent Factor Matrix
        # M : Movie Latent Factor Matrix
        # P : Binary Rating Matrix, user i가 movie j에 대해 평점을 남겼는지의 여부를 나타낸 지 나타낸 행렬
        U = np.random.rand(nu, nf)*0.01
        M = np.random.rand(nm, nf)*0.01
        P = np.copy(R)
        P[P > 0] = 1

        # round_two : 소수점 둘째 자리 반올림 처리
        round_two = np.vectorize(lambda x: round(x, 2))

        # ALS를 활용하여 최적화된 U, M을 찾아낸 후, R_pred 계산
        R_pred = round_two(alternating_least_squares(P, R, U, M, lmda, nu, nm, nf))


    else:
        # method가 올바르지 않은경우 400 코드 return
        print("메소드를 정확히 입력해주세요.")
        return Response(status=status.HTTP_400_BAD_REQUEST)


    # 구한 예상 평점과 영화를 DB에 등록
    # method가 올바르게 입력된 경우(위의 분기에서 else로 빠지지 않는 경우) 여기서 로직이 마무리 됨.
    create_recommended_movie(R, R_pred, nu)
    print("예상 평점 및 영화 DB 등록 완료")
    return Response(status=status.HTTP_201_CREATED)