from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("users/", views.user_list, name="user_list"),
    path("users/<str:username>/", views.user_detail, name="user_detail"),
    path("users/<str:username>/selected", views.user_selected, name="user_selected"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]