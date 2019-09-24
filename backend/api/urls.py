from django.urls import path
from .views import movie_views, scrap_views, admin_views
from accounts import views as account_views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = "api"

urlpatterns = [
    # Auth
    path("signup/", account_views.signup, name="signup"),
    path("users/", account_views.user_list, name="user_list"),
    path("users/<str:username>/", account_views.user_detail, name="user_detail"),
    path('users/<str:username>/ratings/',
         account_views.user_ratings, name='user_ratings'),
    path('users/<str:username>/followings/',
         account_views.user_followings, name='user_followings'),
    path('users/<str:username>/profile/',
         account_views.profile_image, name="profile_image"),
    path('users/related_users/<str:username>/',
         account_views.related_users, name="related_users"),


    path("login/", account_views.login, name="login"),
    path("logout/", account_views.logout, name="logout"),
    path("subscribe/", account_views.subscribe, name="subscribe"),


    # jwt
    path("token/create/", obtain_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("token/refresh/", refresh_jwt_token),

    # movies, ratings
    path('movies/', movie_views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', movie_views.movie_detail,
         name='movie_detail'),
    path('movies/<int:movie_id>/ratings/',
         movie_views.movie_ratings, name='movie_ratings'),
    path('movies/<int:movie_id>/followers/',
         movie_views.movie_followers, name='movie_followers'),
    path('movies/<int:movie_id>/recommendations/',
         movie_views.movie_recommendations, name='movie_recommendations'),
    path('ratings/', movie_views.rating_list, name='rating_list'),
    path('ratings/<int:rating_id>/',
         movie_views.rating_detail, name='rating_detail'),

    path('movies/related_movies/',
         movie_views.related_movies, name="related_movies"),
    path('movies/recommendations/',
         movie_views.refresh_recommendations, name='refresh_recommendations'),

    # admin
    path('admin/movies/', admin_views.movies, name="admin_movies"),
    path('admin/users/', admin_views.users, name="admin_users"),

    # scrap
    path('scrap/', scrap_views.scrap_poster),
]
