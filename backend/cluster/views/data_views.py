# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie, Rating

# Data Processing & Clustering Libs 
import numpy as np
from numpy import dot
from numpy.linalg import norm


'''
movie_views, user_views에서 처리시에 필요한 데이터, 변수들을 저장한 파일
'''

# Variables


# Data Preprocessing
def data_preprocessing(table):
    movies = Movie.objects.all()
    users = User.objects.all()

    # define Index Variables
    ml = movies.last().id
    ul = users.last().id

    # return rating matrix
    if table == 'm':
        movies_data = np.zeros((ml, ul))
        print("movies_data를 받아오는 중입니다.")
        for movie in movies:
            for rating in movie.ratings.all():
                movies_data[movie.id-1][rating.user.id-1] += rating.rating
        
        return movies_data

    elif table == 'u':
        users_data = np.zeros((ul, ml))
        print("users_data를 받아오는 중입니다.")
        for user in users:
            for rating in user.ratings.all():
                users_data[user.id-1][rating.movie.id-1] += rating.rating
        
        return users_data

    else:
        print("table 인자를 정확히 입력해주세요.")


# Update Clustering Data in DB
def update_clustering_data(table, clustering_data):

    if table == 'm':
        movies = Movie.objects.all()
        for movie in movies:
            movie.cluster = clustering_data[movie.id-1]
            movie.save()

    if table == 'u':
        users = User.objects.all()
        for user in users:
            user.cluster = clustering_data[user.id-1]
            user.save()



# K-Means Customized Api (Movie)
def kmeans_custom_clustering_movies(k, iters, movies_data):

    # define variables, data, and function
    ml = Movie.objects.last().id
    ul = User.objects.last().id
   
    clustering_data = np.full((1, ml), -1)[0]
    div = np.vectorize(lambda a, b: round(a/b, 4))
    
    # initialize k of centroids randomly
    centroids = np.random.randint(5, size=(k, ul))


    for _ in range(iters):

        # clustering (find nearest centroid for each movie_data by calculating Euclidean distance)
        for i in range(ml):
            dist = (ul*25)
            cluster = -1
            for j in range(k):
                temp = sum(((movies_data[i])-centroids[j])**2)
                # print("dist: {}, temp: {}".format(dist, temp))              
                if temp < dist:
                    dist = temp
                    cluster = j

            clustering_data[i] = cluster
        
        # adjust centroids
        centroids = np.zeros((k, ul))
        cnt_array = [0 for _ in range(k)]
        
        for i in range(ml):
            cl = clustering_data[i]
            cnt_array[cl] += 1
            centroids[cl] = np.add(centroids[cl], movies_data[i])
            
        for i in range(k):
            cnt = cnt_array[i]
            if cnt == 0:
                continue
            centroids[i] = div(centroids[i], cnt)
            
    return clustering_data



# K-Means Customized Api (User)
def kmeans_custom_clustering_users(k, iters, users_data):

    # define variables, functions and data
    ml = Movie.objects.last().id
    ul = User.objects.last().id
    
    clustering_data = np.full((1, ul), -1)[0]
    div = np.vectorize(lambda a, b: round(a/b, 4))
    
    # initialize k of centroids randomly
    centroids = np.random.randint(5, size=(k, ml)) 
     
    for _ in range(iters):
        
        # clustering (find nearest centroid for each users_data by calculating Euclidean distance)
        for i in range(ul):
            dist = (ml*25)
            cluster = -1
            for j in range(k):
                temp = sum(((users_data[i])-centroids[j])**2)
                # print("dist: {}, temp: {}".format(dist, temp))              
                if temp < dist:
                    dist = temp
                    cluster = j

            clustering_data[i] = cluster

        # adjust centroids
        centroids = np.zeros((k, ml))
        cnt_array = [0 for _ in range(k)]
        
        for i in range(ul):
            cl = clustering_data[i]
            cnt_array[cl] += 1
            centroids[cl] = np.add(centroids[cl], users_data[i])
     
        for i in range(k):
            cnt = cnt_array[i]
            if cnt == 0:
                continue
            
            centroids[i] = div(centroids[i], cnt)
            
    return clustering_data



# cosine similarity
def cos_sim(a, b):
    return round(dot(a, b)/(norm(a)*norm(b)), 2)
