# django
from django.shortcuts import get_object_or_404

# Models
from accounts.models import User
from api.models import Movie, Rating

# Data Processing & Clustering Libs 
import numpy as np


'''
movie_views, user_views에서 처리시에 필요한 데이터, 변수들을 저장한 파일
'''

# Variables
movies_count = Movie.objects.last().id
users_count = User.objects.last().id

# Data Preprocessing
def data_preprocessing(table):
    movies = Movie.objects.all()
    users = User.objects.all()

    print("number of movies: {}, users: {}".format(movies_count, users_count))

    if table == 'm':
        movies_data = np.zeros((movies_count, users_count))
        for movie in movies:
            for rating in movie.ratings.all():
                movies_data[movie.id-1][rating.user.id-1] += rating.rating
        
        return movies_data

    elif table == 'u':
        users_data = np.zeros((users_count, movies_count))
        for user in users:
            for rating in user.ratings.all():
                users_data[user.id-1][rating.movie.id-1] += rating.rating
        
        return users_data

    else:
        print("Movie, User 중 하나를 인자로 넣어야 합니다.")
        return



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
def kmeans_custom_clustering_movies(k, iters):
   
    # define variables, data, and function
    ml = movies_count
    ul = users_count
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
def kmeans_custom_clustering_users(k, iters):
    
    # define variables, functions and data
    ml = movies_count
    ul = users_count
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