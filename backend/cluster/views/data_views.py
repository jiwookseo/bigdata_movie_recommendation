# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie, Rating
from cluster.models import RecommendedMovie

# Data Processing & Clustering Libs 
import numpy as np
from numpy import dot
from numpy.linalg import norm


'''
movie_views, user_views에서 처리시에 필요한 데이터, 변수, 함수들을 정의한 파일
'''


# Create Rating Matrix (Movie-User, User-Movie)
def create_rating_matrix(row):

    movies = Movie.objects.all()
    users = User.objects.all()

    # define Index Variables
    nm = movies.last().id
    nu = users.last().id

    # movie-user rating matrix
    if row == 'm':
        movie_rating_matrix = np.zeros((nm, nu))
        print("영화-평점 데이터를 받아오는 중입니다.")

        for movie in movies:
            for rating in movie.ratings.all():
                movie_rating_matrix[movie.id-1, rating.user.id-1] += rating.rating
        
        print("영화-평점 데이터를 받아왔습니다.")
        return movie_rating_matrix

    # user-movie rating matrix
    elif row == 'u':
        user_rating_matrix = np.zeros((nu, nm))
        print("유저-평점 데이터를 받아오는 중입니다.")

        for user in users:
            for rating in user.ratings.all():
                user_rating_matrix[user.id-1, rating.movie.id-1] += rating.rating
        
        print("유저-평점 데이터를 받아왔습니다.")
        return user_rating_matrix

    else:
        print("row 인자를 정확히 입력해주세요.")




# cosine similarity
def cosine_similarity(a, b):
    return round(dot(a, b)/(norm(a)*norm(b)), 2)


# Create Similarity Matrix (Movie-Movie, User-User)
def create_similarity_matrix(rating_matrix, n):
    
    similarity_matrix = np.zeros((n, n))
    for i in range(n):
        for  j in range(i+1, n):
            similarity = cosine_similarity(rating_matrix[i, :], rating_matrix[j, :])
            similarity_matrix[i, j] = similarity_matrix[j, i] = similarity
        print("유사도 데이터 생성 중, {}/{}".format(i, n))

    return similarity_matrix




# Loss Function
def loss_function(P, R, U, M, lmda):
    UmT = np.matmul(U, np.transpose(M))
    error = np.sum(np.multiply(P, np.square(R - UmT)))
    regularization = lmda * (np.sum(np.square(U)) + np.sum(np.square(M)))
    loss = error + regularization
    return loss


# Optimization
def optimize_user(P, R, U, M, lmda, nu, nf):
    mT = np.transpose(M)
    for i in range(nu):
        Pi = np.diag(P[i])
        mT_Pi_M = np.matmul(np.matmul(mT, Pi), M)
        I = np.dot(lmda, np.identity(nf))
        mT_Ri = np.matmul(mT, R[i])
        U[i] = np.linalg.solve(mT_Pi_M + I, mT_Ri)

def optimize_movie(P, R, U, M, lmda, nm, nf):
    uT = np.transpose(U)
    for j in range(nm):
        Pj = np.diag(P[:, j])
        uT_Pj_U = np.matmul(np.matmul(uT, Pj), U)
        I = np.dot(lmda, np.identity(nf))
        uT_Rj = np.matmul(uT, R[:, j])
        M[j] = np.linalg.solve(uT_Pj_U + I, uT_Rj)


# Alternating Least Squares
def alternating_least_squares(P, R, U, M, lmda, nu, nm, nf):
    for k in range(20):
        if k > 0:
            optimize_user(P, R, U, M, lmda, nu, nf)
            optimize_movie(P, R, U, M, lmda, nm, nf)
        # loss = loss_function(P, R, U, M, lmda)
        print("ALS 실행 중, {}/{}".format(k, 20))
    
    R_pred = np.matmul(U, np.transpose(M))
    return R_pred




# Create New RecommendedMovies and Insert them to DB
def create_recommended_movie(R, R_pred, nu):

    for i in range(nu): 
        # user 없을 시 예외 처리
        try:
            user = User.objects.get(pk=i+1)
        except User.DoesNotExist:
            continue
        
        # 예상 평점 높은 순으로 k개의 영화만 추출
        movies_sorted_by_expected_ratings = np.argsort(R_pred[i])[::-1]
        
        k = 5
        cnt = 1
        selected_movies_list = []
        
        for movie in movies_sorted_by_expected_ratings:
            if cnt > k:
                break
            
            if R[i, movie] > 0:
                continue
            else:
                selected_movies_list.append([movie+1, R_pred[i, movie]])
                cnt += 1
        
        # n개의 영화 및 예상 평점 DB에 등록
        for movie, rating in selected_movies_list:
            try:
                recommended_movie = RecommendedMovie.objects.get(user=user, movie=Movie.objects.get(pk=movie+1))
                if recommended_movie.exp_rating < rating:
                    recommended_movie.exp_rating = rating
                    recommended_movie.save()
            except RecommendedMovie.DoesNotExist:
                recommended_movie = RecommendedMovie(user=user, movie=Movie.objects.get(pk=movie+1), exp_rating=rating)
                recommended_movie.save()
            except Movie.DoesNotExist:
                continue

        print("맞춤 영화 등록 중, {}/{}".format(i, nu))




# Update Clustering Data
def update_clustering_data(row, clustering_data):

    if row == 'm':
        movies = Movie.objects.all()
        for movie in movies:
            movie.cluster = clustering_data[movie.id-1]
            movie.save()

    if row == 'u':
        users = User.objects.all()
        for user in users:
            user.cluster = clustering_data[user.id-1]
            user.save()




# K-Means Customized Api (Movie)
def kmeans_custom_clustering_movies(k, iters, movie_rating_matrix):

    # define variables, data, and function
    nm = Movie.objects.last().id
    nu = User.objects.last().id
   
    clustering_data = np.full((1, nm), -1)[0]
    div = np.vectorize(lambda a, b: round(a/b, 4))
    
    # initialize k of centroids randomly
    centroids = np.random.randint(5, size=(k, nu))


    for _ in range(iters):

        # clustering (find nearest centroid for each movie_data by calculating Euclidean distance)
        for i in range(nm):
            dist = (nu*25)
            cluster = -1
            for j in range(k):
                temp = sum(((movie_rating_matrix[i])-centroids[j])**2)
                # print("dist: {}, temp: {}".format(dist, temp))              
                if temp < dist:
                    dist = temp
                    cluster = j

            clustering_data[i] = cluster
        
        # adjust centroids
        centroids = np.zeros((k, nu))
        cnt_array = [0 for _ in range(k)]
        
        for i in range(nm):
            cl = clustering_data[i]
            cnt_array[cl] += 1
            centroids[cl] = np.add(centroids[cl], movie_rating_matrix[i])
            
        for i in range(k):
            cnt = cnt_array[i]
            if cnt == 0:
                continue
            centroids[i] = div(centroids[i], cnt)
            
    return clustering_data




# K-Means Customized Api (User)
def kmeans_custom_clustering_users(k, iters, user_rating_matrix):

    # define variables, functions and data
    nm = Movie.objects.last().id
    nu = User.objects.last().id
    
    clustering_data = np.full((1, nu), -1)[0]
    div = np.vectorize(lambda a, b: round(a/b, 4))
    
    # initialize k of centroids randomly
    centroids = np.random.randint(5, size=(k, nm)) 
     
    for _ in range(iters):
        
        # clustering (find nearest centroid for each user_rating_matrix by calculating Euclidean distance)
        for i in range(nu):
            dist = (nm*25)
            cluster = -1
            for j in range(k):
                temp = sum(((user_rating_matrix[i])-centroids[j])**2)
                # print("dist: {}, temp: {}".format(dist, temp))              
                if temp < dist:
                    dist = temp
                    cluster = j

            clustering_data[i] = cluster

        # adjust centroids
        centroids = np.zeros((k, nm))
        cnt_array = [0 for _ in range(k)]
        
        for i in range(nu):
            cl = clustering_data[i]
            cnt_array[cl] += 1
            centroids[cl] = np.add(centroids[cl], user_rating_matrix[i])
     
        for i in range(k):
            cnt = cnt_array[i]
            if cnt == 0:
                continue
            
            centroids[i] = div(centroids[i], cnt)
            
    return clustering_data