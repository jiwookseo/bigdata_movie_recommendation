# python, django libraries
import json, datetime
from django.shortcuts import get_object_or_404
from django.db.models import Q

# authentication
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from .jwt import create_token, verify_token, refresh_token

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Model
from .models import User
from api.models import Movie
from cluster.models import RecommendedMovie

# Form, Serializer
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm, CustomUserChangeForm
from api.serializers import MovieSerializer, RatingSerializer
from .serializers import UserSerializer





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
                return Response(data=error, status=status.HTTP_200_OK)
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
        req_name = request.data.get("username", None)
        if req_name:
            req_user = get_object_or_404(User, username=req_name)

            if token == req_user.refresh_token:
                if username != req_name:
                    if not req_user.is_staff:
                        return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

                response = verify_token(token)
                if response.status_code != 200:
                    response = refresh_token(token)
                    if response.status_code == 200:
                        new_token = json.loads(response.text)["token"]
                        req_user.refresh_token = new_token

                if response and response.status_code == 200:
                    change = request.data.get("changeInfo", None)
                    pw = request.data.get("pw", None)
                    if change:
                        form = CustomUserChangeForm(instance=user, data=change)
                        if form.is_valid():
                            form.save()
                        else:
                            error = form.errors.get_json_data()
                            return Response(data=error, status=status.HTTP_200_OK)
                    elif pw:
                        original = pw["original"]
                        if check_password(original, req_user.password):
                            if pw["new1"] == pw["new2"]:
                                req_user.set_password(pw["new1"])
                                req_user.save()
                                auth_login(request, req_user)
                            else:
                                return Response(data={"error": "새 비밀번호가 틀렸습니다."}, status=status.HTTP_200_OK)
                        else:
                            return Response(data={"error": "현재 비밀번호가 틀렸습니다."}, status=status.HTTP_200_OK)
                    else:
                        return Response(data={"error": "입력된 값이 없습니다."}, status=status.HTTP_204_NO_CONTENT)
                    return Response(status=status.HTTP_202_ACCEPTED)
            req_user.refresh_token = ""
            req_user.save()
            auth_logout(request)
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(data={"error": "입력된 값이 없습니다."}, status=status.HTTP_204_NO_CONTENT)

    if request.method == "DELETE":
        token = request.data.get("token", None)
        req_name = request.data.get("username", None)

        if req_name:
            req_user = get_object_or_404(User, username=req_name)

            if token == req_user.refresh_token:
                if username != req_name:
                    if not req_user.is_staff:
                        return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

                response = verify_token(token)
                if response.status_code != 200:
                    response = refresh_token(token)
                    if response.status_code == 200:
                        new_token = json.loads(response.text)["token"]
                        req_user.refresh_token = new_token

                if response and response.status_code == 200:
                    user.delete()
                    return Response(status=status.HTTP_202_ACCEPTED)

            user.refresh_token = ""
            user.save()
            auth_logout(request)
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(data={"error": "입력값이 없습니다."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_ratings(request, username):
    user = get_object_or_404(User, username=username)
    id = request.GET.get("movieId", None)
    if id:
        movie = get_object_or_404(Movie, id=id)
        rating = user.ratings.filter(movie=movie)
        serializer = RatingSerializer(rating, many=True)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    serializer = RatingSerializer(user.ratings.all(), many=True)
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def profile_image(request, username):
    user = get_object_or_404(User, username=username)
    image = request.data.get('image', None)
    if image:
        user.image = image
        user.save()
        print('http://localhost:8000' + user.image.url)
        return Response(data={"image": 'http://localhost:8000' + user.image.url}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def user_followings(request, username):
    user = get_object_or_404(User, username=username)
    serializer = MovieSerializer(user.followings, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def related_users(request, username):
    user = get_object_or_404(User, username=username)
    query = Q(cluster__exact=user.cluster)
    query.add(~Q(username=username), query.AND)

    related_users = User.objects.filter(query)[:10]
    serializer = UserSerializer(related_users, many=True)
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(["POST"])
def subscribe(request):
    username = request.data.get("username", None)
    token = request.data.get("token", None)

    user = get_object_or_404(User, username=username)

    if token == user.refresh_token:
        response = verify_token(token)
        if response.status_code != 200:
            response = refresh_token(token)
            if response.status_code == 200:
                new_token = json.loads(response.text)["token"]
                user.refresh_token = new_token

        if response and response.status_code == 200:
            if user.subscribe:
                if datetime.datetime.now() - user.subscribe_at < datetime.timedelta(30):
                    return Response(status=status.HTTP_400_BAD_REQUEST)

            user.subscribe = True
            user.subscribe_at = datetime.datetime.now()
            user.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    user.refresh_token = ""
    user.save()
    auth_logout(request)
    return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

@api_view(["POST"])
def login(request):
    user = request.data.get("login", None)
    admin = request.data.get("admin", None)
    form = CustomUserAuthenticationForm(request, data=user)
    if form.is_valid():

        if admin:
            admin = form.get_user()
            if not admin.is_staff:
                return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        token = create_token(user)
        token = token.json()["token"]
        user = form.get_user()
        user.refresh_token = token

        if user.subscribe:
            if datetime.datetime.now() - user.subscribe_at > datetime.timedelta(30):
                user.subscribe = False

        user.save()

        auth_login(request, user)

        response = {
            "token": token,
            "username": user.username,
            "is_staff": user.is_staff,
            "subscribe": user.subscribe
        }

        return Response(data=response, status=status.HTTP_202_ACCEPTED)
    else:
        error = form.errors.get_json_data()
        return Response(data=error, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@login_required
@api_view(["POST"])
def logout(request):
    username = request.data.get("username", None)
    user = get_object_or_404(User, username=username)
    user.refresh_token = ""
    user.save()

    auth_logout(request)
    return Response(status=status.HTTP_202_ACCEPTED)



# 사용자 별 맞춤 추천영화
@login_required
@api_view(['GET'])
def recommended_movies(request, username):
    query = Q()

    user = get_object_or_404(User, username=username)
    recommended_movies_data = RecommendedMovie.objects.filter(user=user).values('movie')[:3]

    for data in recommended_movies_data:
        query.add(Q(pk__exact=data['movie']), query.OR)

    recommended_movies = Movie.objects.filter(query)
    serializer = MovieSerializer(recommended_movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
