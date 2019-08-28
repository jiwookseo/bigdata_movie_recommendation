# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from django.contrib.auth.models import User
from api.models import Movie, Profile, Rating

# Data Processing Tools
import numpy as np
import pandas as pd

# Clustering
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning



'''
클러스터링 및 클러스터링의 Data를 DB에 저장하기.
Clustering된 데이터를 가져오는 것은 모델별 views에서 시행.
'''



# Data Processing
def data_preprocessing(table):
  movies = Movie.objects.all()
  users = User.objects.all()
  
  if table == 'm':
      movies_data = [[0]*users.count() for _ in range(movies.count())]
      for movie in movies:
        for rating in movie.ratings.all():
          movies_data[movie.id-1][rating.user.id-1] += rating.rating
      
      return movies_data

  if table == 'u':
      users_data = [[0]*movies.count() for _ in range(users.count())]
      for user in users:
          for rating in user.ratings.all():
              users_data[user.id-1][rating.movie.id-1] += rating.rating
      
      return users_data



# Update Clustering Data
def update_clustering_data(table, clustering_data):

  # if table == 'm':
  #     movies = Movie.objects.all()
  #     for movie in movies:
  #         movie.cluster = clustering_data[movie.id]
  #         movie.save()
  
  # if table == 'u':
  #     users = User.objects.all()
  #     for user in users:
  #         user.cluster = clustering_data[user.id]
  #         user.save()
  pass



# Movie Clustering
@api_view(['POST'])
def movie_clustering(request, method, k):
    movies_data = data_preprocessing('m')
    
    # K-Means
    if method == 0:
        model = KMeans(n_clusters=k, init="random", random_state=0)
        model.fit(movies_data)
        clustering_data = model.predict(movies_data) 

    # Hierarchy
    if method == 1:
        model = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage='ward')
        clustering_data = model.fit_predict(movies_data)

    # EM
    if method == 2:
        model = GaussianMixture(n_components=k, init_params='random', random_state=0, max_iter=100)
        with ignore_warnings(category=ConvergenceWarning):
            model.fit(movies_data)
        clustering_data = model.predict(movies_data)
      
    update_movie_clustering_data('m', clustering_data)
    print(clustering_data)

    return Response(status=status.HTTP_201_CREATED)



# User Clustering
@api_view(['POST'])
def user_clustering(request, method, k):
    users_data = data_preprocessing('u')

    # K-Means
    if method == 0:
        model = KMeans(n_clusters=k, init="random", random_state=0)
        model.fit(users_data)
        clustering_data = model.predict(users_data)

    # Hierarchy
    if method == 1:
        model = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage='ward')
        clustering_data = model.fit_predict(users_data)

    # EM
    if method == 2:
        model = GaussianMixture(n_components=k, init_params='random', random_state=0, max_iter=100)
        with ignore_warnings(category=ConvergenceWarning):
            model.fit(users_data)
        clustering_data = model.predict(users_data)

    update_clustering_data('u', clustering_data)
    print(clustering_data)
    
    return Response(status=status.HTTP_201_CREATED)


# test code
if __name__ == '__main__':
    pass