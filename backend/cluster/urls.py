from django.urls import path
from .views import movie_views, user_views

app_name = "cluster"


urlpatterns = [
    # Clustering : Movie
    path('movies/', movie_views.movie_clustering, name="movie_clustering"),

    # Clustering : User
    path('users/', user_views.user_clustering, name="user_clustering"),

    # Collaborative Filtering
    path('users/recommended_movies/', user_views.recommended_movies, name="recm_movies"),
]