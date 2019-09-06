# python 
import random

# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie, Rating

# Data Processing Tools
import numpy as np

# Clustering
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning



movies_count = 3952

# Data Preprocessing
def data_preprocessing(table):
    movies = Movie.objects.all()
    users = User.objects.all()

    print("number of movies: {}, users: {}".format(movies.count(), users.count()))

    if table == 'm':
        movies_data = np.zeros((movies_count, users.count()))
        for movie in movies:
            for rating in movie.ratings.all():
                movies_data[movie.id-1][rating.user.id-1] += rating.rating
        
        return movies_data

    elif table == 'u':
        users_data = np.zeros((users.count(), movies_count))
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
    ul = users.count()
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



# Movie Clustering
@api_view(['POST'])
def movie_clustering(request):
    try:
        movies_data = data_preprocessing('m')
        print("data preprocessing is completed")
        method = request.data.get('method')
        k = request.data.get('k', 7)
        
        # K-Means
        if method == 'km':
            model = KMeans(n_clusters=k, init="random", random_state=0)
            model.fit(movies_data)
            clustering_data = model.predict(movies_data) 

        # Hierarchy
        elif method == 'hr':
            model = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage='ward')
            clustering_data = model.fit_predict(movies_data)

        # EM
        elif method == 'em':
            model = GaussianMixture(n_components=k, init_params='random', random_state=0, max_iter=100)
            with ignore_warnings(category=ConvergenceWarning):
                model.fit(movies_data)
            clustering_data = model.predict(movies_data)

        # K-Means Customized
        elif method == 'kmc':
            clustering_data = kmeans_custom_clustering_movies(k, 100)

        else:
            print("method를 정확히 표기해주세요.")

        print("clustering is completed")
        update_clustering_data('m', clustering_data)
        print("to update clustering data is completed")

        return Response(status=status.HTTP_201_CREATED)
    
    except ConnectionAbortedError:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

# K-Means Customized Api (User)
def kmeans_custom_clustering_users(k, iters):
    
    # define variables, functions and data
    ml = movies_count
    ul = users.count()
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
        clustering_data = kmeans_custom_clustering_users(k, 100)

    else:
        print("method를 정확히 표기해주세요.")

    print("clustering is completed")
    update_clustering_data('u', clustering_data)        
    print("to update clustering data is completed")
    
    return Response(status=status.HTTP_201_CREATED)

