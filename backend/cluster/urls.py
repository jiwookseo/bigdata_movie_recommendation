from django.urls import path
from .views import movie_views, user_views, data_views

app_name = "cluster"

urlpatterns = [
    # Movie
    # clustering movies
    path('movies/', movie_views.movie_clustering, name="movie_clustering"),

    # movie similarity 
    path('movie_similarity/', movie_views.movie_similarity, name="movie_similarity"),
    path('similar_movies/<int:movie_id>/', movie_views.similar_movies, name="similar_movies"),


    # User
    # clustering users
    path('users/', user_views.user_clustering, name="user_clustering"),
    
    # user similarity
    path('user_similarity/', user_views.user_similarity, name="user_similarity"),
    path('similar_users/<int:user_id>/', user_views.similar_users, name="similar_users"),
]