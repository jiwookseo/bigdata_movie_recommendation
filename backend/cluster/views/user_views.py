# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from accounts.models import User
from api.models import Movie
from cluster.models import UserSimilarity

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

    print("clustering is completed")
    update_clustering_data('u', clustering_data)        
    print("to update clustering data is completed")
    
    return Response(status=status.HTTP_201_CREATED)



# User Similarity
@api_view(['POST'])
def user_similarity(request):

    # define Index Variables
    ml = Movie.objects.last().id
    ul = User.objects.last().id

    # get movie rating matrix
    users_data = data_preprocessing('u')

    for i in range(ul):
        for j in range(i+1, ul): 
            user_i_ratings = users_data[i]
            user_j_ratings = users_data[j]
            similarity = cos_sim(user_i_ratings, user_j_ratings)
            
            if isinstance(similarity, float) and similarity >= 0.25:
                try:
                    user_similarity = UserSimilarity.objects.get(user_former=User.objects.get(pk=i+1), user_latter=User.objects.get(pk=j+1))
                except UserSimilarity.DoesNotExist:
                    user_similarity = UserSimilarity(user_former=User.objects.get(pk=i+1), user_latter=User.objects.get(pk=j+1))
                
                user_similarity.similarity = similarity
                user_similarity.save()
            else:
                continue
            
        print("loading... {}/{}".format(i, ul))
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def similar_users(request, user_id):
    pass