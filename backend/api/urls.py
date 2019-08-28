from django.conf.urls import url
from .views import movie_views
from .views import auth_views
from .views import rating_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.rating, name='ratings_list'),
]
