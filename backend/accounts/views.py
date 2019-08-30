from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from api.serializers import RatingSerializer
from .models import User
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm,  CustomUserChangeForm


#회원가입
@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        users = request.data.get('profiles', None)
        if len(users) > 1:
            for user in users:
                form = CustomUserCreateForm(data=user)
                if form.is_valid():
                    form.save()
        else:
            form = CustomUserCreateForm(data=users)
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


@api_view(["GET"])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@login_required
@api_view(["PUT", "DELETE"])
def user_selected(request, username):
    if request.method == "PUT":
        change = request.get.data("changeInfo", None)
        user = get_object_or_404(User, username=username)
        form = CustomUserChangeForm(instance=user, data=change)
        if form.is_valid():
            form.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        user = get_object_or_404(User, username=username)
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


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
        auth_login(request, form.get_user())

        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(["POST"])
def logout(request):
    auth_logout(request)
    return Response(status=status.HTTP_200_OK)