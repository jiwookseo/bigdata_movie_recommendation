# django
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie
from cluster.models import MovieSimilarity

# Variables and Functions For Data Processing : data_views.py
from .data_views import data_preprocessing, update_clustering_data, kmeans_custom_clustering_movies
from .data_views import cos_sim

# Data Processing & Clustering Libs 
import numpy as np

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning



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
            clustering_data = kmeans_custom_clustering_movies(k, 100, movies_data)

        else:
            print("method를 정확히 표기해주세요.")

        print("clustering is completed")
        update_clustering_data('m', clustering_data)
        print("to update clustering data is completed")

        return Response(status=status.HTTP_201_CREATED)
    
    except ConnectionAbortedError:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# Movie Similarity
@api_view(['POST'])
def movie_similarity(request):

    # define Index Variables
    ml = Movie.objects.last().id
    ul = User.objects.last().id

    # get movie rating matrix
    movies_data = data_preprocessing('m')

    for i in range(ml):
        for j in range(i+1, ml): 
            movie_i_ratings = movies_data[i]
            movie_j_ratings = movies_data[j]
            similarity = cos_sim(movie_i_ratings, movie_j_ratings)

            if isinstance(similarity, float) and similarity >= 0.75:
                try:
                    movie_similarity = MovieSimilarity.objects.get(movie_former=Movie.objects.get(pk=i+1), movie_latter=Movie.objects.get(pk=j+1))
                except:
                    movie_similarity = MovieSimilarity(movie_former=Movie.objects.get(pk=i+1), movie_latter=Movie.objects.get(pk=j+1))

                movie_similarity.similarity = similarity
                movie_similarity.save()
            else:
                continue

        print("loading... {}/{}".format(i, ml))
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def similar_movies(request, movie_id):
    pass