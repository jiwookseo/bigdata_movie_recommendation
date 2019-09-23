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



# Records of Recommended Movies including expected ratings for Users.
# Algorithms : KNN - Movie Based, User Based
@api_view(['POST'])
def recm_movies(request, method):

    # Step 0. 필요한 변수 정의 및 데이터 생성
    
    # 인덱스 변수 정의
    ml = Movie.objects.last().id
    ul = User.objects.last().id

    # 유사한 데이터를 의미하는 Neighbor의 수, K 정의
    k = 10

    # user-rating matrix인 users_data_origin 생성 및 예상 평점도 포함할 대조본인 users_data_exp_rating
    users_data_origin = data_preprocessing('u')
    users_data_exp_rating = np.copy(users_data_origin)

    # KNN - Movie Based
    if method == 'mb':

        # Step 1. 유사도 데이터 생성을 위한 movie-rating matrix 생성
        movies_data = data_preprocessing('m')
        print("1/4, 변수 및 데이터 생성 완료.")

        # Step 2. 영화 유사도 데이터 생성
        movie_similarity = np.zeros((ml, ml))

        for i in range(ml):
            for j in range(i+1, ml):  
                cosine_similarity = round(cos_sim(movies_data[i, :], movies_data[j, :]), 2)
                movie_similarity[i, j] = cosine_similarity
                movie_similarity[j, i] = cosine_similarity

            print("2/4, {}/{}".format(i, ml))                 
        print("2/4, 영화 유사도 데이터 생성 완료")

        # Step 3. 평점 계산 및 입력
        for i in range(ul):

            # User가 존재하는지 체크, 없으면 패스
            try:
                user = User.objects.get(pk=i+1)
            except:
                continue

            # User가 있을 경우 Movie에 대해 순회하며 예상 평점 계산 (user i+1 -> movie j+1)
            for j in range(ml):
                
                # Movie가 DB에 존재하는지 확인, 없으면 패스
                # try:
                #     movie = Movie.objects.get(pk=j+1)
                # except:
                #     continue
                
                # 만약 평점을 남겼다면, 예상평점을 구할 이유가 없으므로 패스, 
                if users_data_origin[i, j] > 0:
                    continue
                    
                # 현재 영화와 유사한 영화 순으로 정렬, 평점을 위한 cnt와 total 변수 초기화
                similar_movies = np.argsort(movie_similarity[j, :])[::-1]
                total = 0
                cnt = 1
                
                for mv in similar_movies:         
                    if cnt > k:
                        break
                        
                    # i+1의 유저가 해당 영화에 평점을 남겼다면 total과 cnt에 합산.
                    if users_data_origin[i, mv] > 0:
                        total += users_data_origin[i, mv]
                        cnt += 1
                        
                # 평점 구하기 (total / cnt)
                if cnt == 0:
                    exp_rating = 0
                else:
                    exp_rating = round((total / cnt), 2)

                users_data_exp_rating[i, j] = exp_rating
            
            print("3/4, {}/{}".format(i, ul))
        print("3/4, 평점 계산 및 입력 완료")

        # Step 4. 구한 예상 평점과 영화를 DB에 등록
        for i in range(ul):
            
            # user 없을 시 예외 처리
            try:
                user = User.objects.get(pk=i+1)
            except User.DoesNotExist:
                continue
            
            # 예상 평점 높은 순으로 n개의 영화만 추출
            movie_info_data = np.argsort(users_data_exp_rating[i])[::-1]
            
            n = 5
            cnt = 1
            mv_rating_list = []
            
            for mv in movie_info_data:
                if cnt > n:
                    break
                
                if users_data_origin[i, mv] > 0:
                    continue
                else:
                    mv_rating_list.append([mv+1, users_data_exp_rating[i, mv]])
                    cnt += 1
            
            # n개의 영화 및 예상 평점 DB에 등록
            for mv, rating in mv_rating_list:
                try:
                    recm_movie = RecommendedMovie.objects.get(user=user, movie=Movie.objects.get(pk=mv+1))
                    if recm_movie.exp_rating < rating:
                        recm_movie.exp_rating = rating
                        recm_movie.save()
                except RecommendedMovie.DoesNotExist:
                    exp_rating = RecommendedMovie(user=user, movie=Movie.objects.get(pk=mv+1), exp_rating=rating)
                    exp_rating.save()
                except Movie.DoesNotExist:
                    continue

            print("4/4, {}/{}".format(i, ul))
        print("4/4, 예상 평점 및 영화 DB 등록 완료")
        return Response(status=status.HTTP_201_CREATED)

                
    # KNN - User Based
    elif method == 'ub':
        users_data_origin = data_preprocessing('u')
        users_data_exp_rating = np.copy(users_data_origin)
        print("1/4, 변수 및 데이터 생성 완료.")


        # Step 2. 영화 유사도 데이터 생성
        user_similarity = np.zeros((ul, ul))
        for i in range(ul):
            for j in range(i+1, ul):      
                cosine_similarity = cos_sim(users_data_origin[i], users_data_origin[j])
                user_similarity[i, j] = cosine_similarity
                user_similarity[j, i] = cosine_similarity
            
            print("2/4, {}/{}".format(i, ul))                  
        print("2/4, 유저 유사도 데이터 생성 완료")   


        # Step 3. 평점 계산 및 입력
        for i in range(ul):
            for j in range(ml):
                # user i+1 -> movie j+1
                
                # 만약 평점을 남겼다면, 예상평점을 구할 이유가 없으므로 패스, 
                if users_data_origin[i, j] > 0:
                    continue
                
                # 유사한 유저들 순으로 정렬, 평점을 위한 cnt와 total 변수 초기화
                similar_users = np.argsort(user_similarity[i])[::-1]
                cnt = 0
                total = 0
                
                for user in similar_users:
                    # k명 까지만 계산에 포함한다.
                    if cnt > k:
                        break
                        
                    # 해당 유저가 평점을 남겼다면?
                    if users_data_origin[user, j] > 0:
                        total += users_data_origin[user, j]
                        cnt += 1
            
                # 평점 구하기 (total / cnt), division by zero 예외 처리
                if cnt == 0:
                    exp_rating = 0
                else:
                    exp_rating = round((total / cnt), 2)
                
                # 구한 평점을 users_data에 넣기
                users_data_exp_rating[i, j] = exp_rating

            print("3/4, {}/{}".format(i, ul))
        print("3/4, 평점 계산 및 입력 완료")


        # Step 4. 구한 예상 평점과 영화를 DB에 등록
        for i in range(ul):
            # user 없을 시 예외 처리
            try:
                user = User.objects.get(pk=i+1)
            except User.DoesNotExist:
                continue
                
            movie_info_data = np.argsort(users_data_exp_rating[i])[::-1]
            
            k = 5
            cnt = 1
            mv_rating_list = []
            
            for mv in movie_info_data:
                if cnt > k:
                    break
                
                if users_data_origin[i, mv] > 0 or users_data_exp_rating[i, mv] == 5:
                    continue
                else:
                    mv_rating_list.append([mv+1, users_data_exp_rating[i, mv]])
                    cnt += 1
                    
            for mv, rating in mv_rating_list:
                try:
                    recm_movie = RecommendedMovie.objects.get(user=user, movie=Movie.objects.get(pk=mv+1))
                    if recm_movie.exp_rating < rating:
                        recm_movie.exp_rating = rating
                        recm_movie.save()
                except RecommendedMovie.DoesNotExist:
                    exp_rating = RecommendedMovie(user=user, movie=Movie.objects.get(pk=mv+1), exp_rating=rating)
                    exp_rating.save()
                except Movie.DoesNotExist:
                    continue


            print("4/4, {}/{}".format(i, ul))
        print("4/4, 예상 평점 및 영화 DB 등록 완료")
        return Response(status=status.HTTP_201_CREATED)

    else:
        print("메소드를 정확히 입력해주세요.")
        return Response(status=status.HTTP_400_BAD_REQUEST)