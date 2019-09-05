from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import MovieSerializer, RatingSerializer
from .jwt import create_token, verify_token, refresh_token
from .serializers import UserSerializer
from .models import User
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm, CustomUserChangeForm
from django.db.models import Q
import json

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
                error = form.errors.get_json_data()
                return Response(data=error, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        token = request.data.get("token", None)
        name = request.data.get("username", None)
        if name != None:
            check = User.objects.get(username=name)

            if token != check.refresh_token:
                return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            if username != name or not check.is_staff:
                return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            response = verify_token(token)
            if response.status_code != 200:
                response = refresh_token(token)
                new_token = json.loads(response.text)["token"]
                check.refresh_token = new_token

            if response and response.status_code == 200:
                change = request.data.get("changeInfo", None)
                pw = request.data.get("pw", None)
                if change:
                    form = CustomUserChangeForm(instance=user, data=change)
                    if form.is_valid():
                        form.save()
                    else:
                        error = form.errors.get_json_data()
                        return Response(data=error, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
                elif pw:
                    original = pw["original"]
                    if check_password(original, check.password):
                        if pw["new1"] == pw["new2"]:
                            check.set_password(pw["new1"])
                            check.save()
                            auth_login(request, check)
                        else:
                            return Response(data={"error": "새 비밀번호가 틀렸습니다."}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
                    else:
                        return Response(data={"error": "현재 비밀번호가 틀렸습니다."}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
                else:
                    return Response(data={"error": "입력된 값이 없습니다."}, status=status.HTTP_204_NO_CONTENT)
                return Response(status=status.HTTP_200_OK)
            check.refresh_token = ""
            check.save()
            auth_logout(request)
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(data={"error": "입력된 값이 없습니다."}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    if request.method == "DELETE":
        token = request.data.get("token", None)
        name = request.data.get("username", None)

        if name != None:
            check = User.objects.get(username=name)

            if token != check.refresh_token:
                return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            if not check.is_staff or username != name:
                return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            response = verify_token(token)
            if response.status_code != 200:
                response = refresh_token(token)
                new_token = json.loads(response.text)["token"]
                check.refresh_token = new_token

            if response and response.status_code == 200:
                user.delete()
                return Response(status=status.HTTP_200_OK)

            user.refresh_token = ""
            user.save()
            auth_logout(request)
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_ratings(request, username):
    user = get_object_or_404(User, username=username)
    serializer = RatingSerializer(user.ratings, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_followings(request, username):
    user = get_object_or_404(User, username=username)
    serializer = MovieSerializer(user.followings, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def related_users(request, user_id):
    user = get_object_or_404(User, id=user_id)
    query = Q(cluster__exact=user.cluster)
    query.add(~Q(id=user_id), query.AND)
    
    related_users = User.objects.filter(query)[:10]
    serializer = UserSerializer(related_users, many=True)
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(["POST"])
def login(request):
    user = request.data.get("login", None)
    form = CustomUserAuthenticationForm(request, data=user)
    if form.is_valid():
        token = create_token(user)
        token = token.json()["token"]
        user = form.get_user()
        user.refresh_token = token
        user.save()

        auth_login(request, user)

        response = {
            "token": token,
            "username": user.username,
            "is_staff": user.is_staff
        }

        return Response(data=response, status=status.HTTP_200_OK)
    else:
        error = form.errors.get_json_data()
        print(error)
        return Response(data=error, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@login_required
@api_view(["POST"])
def logout(request):
    username = request.data.get("username", None)
    user = User.objects.get(username=username)
    user.refresh_token = ""
    user.save()

    auth_logout(request)
    return Response(status=status.HTTP_200_OK)
