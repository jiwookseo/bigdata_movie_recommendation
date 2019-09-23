from django.urls import path
from .views import movie_views, user_views

app_name = "cluster"


urlpatterns = [
    # Movie
    path('movies/', movie_views.movie_clustering, name="movie_clustering"),

    # User
    path('users/', user_views.user_clustering, name="user_clustering"),
    path('users/recm_movies/<str:method>/', user_views.recm_movies, name="recm_movies"),
]