from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating
from django.contrib.auth.models import User
from api.serializers import MovieSerializer, RatingSerializer
import matplotlib.pyplot as plt
from rest_framework.response import Response
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from scipy.sparse import csr_matrix


def test(request):
    method = request.GET.get('method', None)
    # 유저 평점 유사도로 k-means clustering
    users = User.objects.all()
    data = np.zeros((200, 4000))
    for i in range(17, 217):
        for rating in users[i - 17].ratings.all():
            data[i - 17, rating.movie_id] = rating.score
    # 영화 평점 유사도로 k-means clustering
    # movies = Movie.objects.all()
    # data = np.zeros((len(movies), 200))
    # for i in range(len(movies)):
    #     for rating in movies[i].ratings.all():
    #         data[i, rating.user_id - 17] = rating.score
    n = r = 10
    if method == "hierarchical":
        clustering = AgglomerativeClustering(n_clusters=n).fit(data)
        labels = clustering.labels_
    elif method == "em":
        clustering = GaussianMixture(n_components=n, random_state=r).fit(data)
        labels = clustering.predict(data)
    else:
        clustering = KMeans(n_clusters=n, random_state=r).fit(csr_matrix(data))
        centroids = clustering.cluster_centers_
        labels = clustering.labels_
        print(centroids)
    print(labels)
