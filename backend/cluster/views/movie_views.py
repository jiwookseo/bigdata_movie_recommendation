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
from .data_views import create_rating_matrix, update_clustering_data, kmeans_custom_clustering_movies
from .data_views import cosine_similarity

# Data Processing & Clustering Libs 
import numpy as np

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning



# 영화 페이지의 유사한 영화 데이터 생성
# Movie Clustering
# Algorithms : K-Means, Hierarchy, EM
@api_view(['POST'])
def movie_clustering(request):
    movies_data = create_rating_matrix('m')
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
        return Response(status=status.HTTP_400_BAD_REQUEST)

    print("clustering is completed")
    update_clustering_data('m', clustering_data)
    print("to update clustering data is completed")

    return Response(status=status.HTTP_201_CREATED)