from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import RatingSerializer
from .jwt import create_token, verify_token, refresh_token
from .serializers import UserSerializer
from .models import User
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm,  CustomUserChangeForm


# 회원가입
@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        users = request.data.get('profiles', None)
        for user in users:
            form = CustomUserCreateForm(data=user)
            if form.is_valid():
                form.save()

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)

    if request.method == "GET":
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    if request.method == "PUT":
        token = request.get.data("token", None)
        name = request.get.data("username", None)

        if name != None:
            user = User.objects.get(username=name)
            response = verify_token(token)
            if response.status_code == 200 and username == name or user.is_staff:
                user = get_object_or_404(User, username=username)
                change = request.get.data("changeInfo", None)
                pw = request.get.data("pw", None)
                if change:
                    form = CustomUserChangeForm(instance=user, data=change)
                    if form.is_valid():
                        form.save()
                    else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                elif pw:
                    form = CustomUserChangePwForm(instance=user, data=pw)
                    if form.is_valid():
                        form.save()
                    else:
                        return Response(status=status.HTTP_401_UNAUTHORIZED)
                user = get_object_or_404(User, username=username)
                serializer = UserSerializer(user)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        token = request.get.data("token", None)
        name = request.get.data("username", None)

        if name != None:
            user = User.objects.get(username=name)
            response = verify_token(token)
            if response.status_code == 200 and username == name or user.is_staff:
                user.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def user_ratings(request, username):
    user = get_object_or_404(User, username=username)
    serializer = RatingSerializer(user.ratings, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def login(request):
    user = request.data.get("login", None)
    form = CustomUserAuthenticationForm(request, data=user)
    if form.is_valid():
        response = create_token(user)
        token = response.json()["token"]

        user = form.get_user()
        user.refresh_token = token
        user.save()

        auth_login(request, user)

        return Response(data=response.json(), status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(["POST"])
def logout(request):
    auth_logout(request)
    return Response(status=status.HTTP_200_OK)