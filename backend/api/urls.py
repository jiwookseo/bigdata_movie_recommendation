from django.urls import path
from api.views import movie_views, auth_views, rating_views, clustering_views



app_name = "api"

urlpatterns = [
    # Auth
    path('users/', auth_views.user_list, name='user_list'),
    path('users/<str:username>/', auth_views.user_detail, name='user_detail'),
    path('users/<str:username>/ratings/',
         auth_views.user_ratings, name='user_ratings'),

    # movies, ratings
    path('movies/', movie_views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', movie_views.movie_detail,
         name='movie_detail'),
    path('movies/<int:movie_id>/ratings/',
         movie_views.movie_ratings, name='movie_rating_list'),
    path('ratings/', movie_views.rating_list, name='rating_list'),
    path('ratings/<int:rating_id>/',
         movie_views.rating_detail, name='rating_detail'),

    # clustering
    path('clustering/movies/<str:method>/<int:k>', clustering_views.movie_clustering, name="movie_clustering"),
    path('clustering/users/<str:method>/<int:k>', clustering_views.user_clustering, name="user_clustering"),
]
