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



# Movie Clustering

def movie_data_preprocessing():
  movies = Movie.objects.all()
  users = User.objects.all()
  
  movies_data = [[0]*users.count() for _ in range(movies.count())]
  for movie in movies:
    for rating in movie.ratings.all():
      movies_data[movie.id-1][rating.user.id-1] += rating.rating
  
  return movies_data


def update_movie_clustering_data(clustering_data):
  # movies = Movie.objects.all()
  # for movie in movies:
  #   movie.cluster = clustering_data[movie.id]
  #   movie.save()
  pass



@api_view(['POST'])
def movie_kmeans_clustering(request):
  movies_data = movie_data_preprocessing()
  
  k = request.data.get('k', 7)
  model = KMeans(n_clusters=k, init="random", random_state=0)
  model.fit(movies_data)
  clustering_data = model.predict(movies_data) 

  update_movie_clustering_data(clustering_data)
  print(clustering_data)

  return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def movie_hierarchy_clustering(request):
  movies_data = movie_data_preprocessing()
  
  k = request.data.get('k', 7)
  model = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage='ward')
  clustering_data = model.fit_predict(movies_data)

  update_movie_clustering_data(clustering_data)
  print(clustering_data)

  return Response(status=status.HTTP_201_CREATED)
  

@api_view(['POST'])
def movie_em_clustering(reqeust):
  movies_data = movie_data_preprocessing()
  
  k = request.data.get('k', 7)
  model = GaussianMixture(n_components=k, init_params='random', random_state=0, max_iter=100)
  with ignore_warnings(category=ConvergenceWarning):
        model.fit(movies_data)
  clustering_data = model.predict(movies_data)

  update_movie_clustering_data(clustering_data)
  print(clustering_data)

  return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def movie_kmeans_customized_clustering(request):
  pass



# User Clustering

def user_data_preprocessing():
  movies = Movie.objects.all()
  users = User.objects.all()

  users_data = [[0]*movies.count() for _ in range(users.count())]
  for user in users:
    for rating in user.ratings.all():
      users_data[user.id-1][rating.movie.id-1] += rating.rating
  
  return users_data


def update_user_clustering_data(clustering_data):
  # users = User.objects.all()
  # for user in users:
  #   user.cluster = clustering_data[user.id]
  #   user.save()
  pass


@api_view(['POST'])
def user_kmeans_clustering(request):
  users_data = user_data_preprocessing()

  k = request.data.get('k', 7)
  model = KMeans(n_clusters=k, init="random", random_state=0)
  model.fit(users_data)
  clustering_data = model.predict(users_data)

  update_user_clustering_data(clustering_data)
  print(clustering_data)
  
  return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_hierarchy_clustering(request):
  users_data = user_data_preprocessing()

  k = request.data.get('k', 7)
  model = AgglomerativeClustering(n_clusters=k, affinity="euclidean", linkage='ward')
  clustering_data = model.fit_predict(users_data)

  update_user_clustering_data(clustering_data)
  print(clustering_data)

  return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_em_clustering(reqeust):
  users_data = user_data_preprocessing()

  k = request.data.get('k', 7)
  model = GaussianMixture(n_components=k, init_params='random', random_state=0, max_iter=100)
  with ignore_warnings(category=ConvergenceWarning):
        model.fit(users_data)
  clustering_data = model.predict(users_data)

  update_movie_clustering_data(clustering_data)
  print(clustering_data)

  return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_kmeans_customized_clustering(request):
  pass


  
