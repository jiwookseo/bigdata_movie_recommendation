# Python Modules
from datetime import datetime
import json

# Django
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# JWT
from accounts.jwt import verify_token, refresh_token

# Models
from api.models import Movie, Rating, Recommendation
from accounts.models import User

# Serializers
from accounts.serializers import UserSerializer
from api.serializers import MovieSerializer, RatingSerializer


@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        total = len(movies)

        # recommend by age, occupation, gender
        age = request.GET.get("age", None)
        username = request.GET.get("username", None)
        occupation = request.GET.get("occupation", None)
        gender = request.GET.get("gender", None)
        limit = int(request.GET.get("limit", 10))
        start = int(request.GET.get("start", 0))
        if username:
            movies = []
            user = get_object_or_404(User, username=username)
            for rating in user.ratings.all().order_by("-rating")[start:limit]:
                movies.append(rating.movie)

            serializer = MovieSerializer(movies, many=True)
            data = {"data": serializer.data,
                    "total": total, "start": start, "limit": limit}
            return Response(data=data, status=status.HTTP_200_OK)

        elif age:
            rec = get_object_or_404(Recommendation, type="age", value=age)
            total = len(rec.movies.all())
            movies = rec.movies.all()[start: start + limit]
            serializer = MovieSerializer(movies, many=True)
            data = {"data": serializer.data,
                    "total": total, "start": start, "limit": limit, "value": age}
            return Response(data=data, status=status.HTTP_200_OK)
        elif occupation:
            rec = get_object_or_404(
                Recommendation, type="occupation", value=occupation)
            total = len(rec.movies.all())
            movies = rec.movies.all()[start: start + limit]
            serializer = MovieSerializer(movies, many=True)
            data = {"data": serializer.data,
                    "total": total, "start": start, "limit": limit, "value": occupation}
            return Response(data=data, status=status.HTTP_200_OK)
        elif gender:
            rec = get_object_or_404(
                Recommendation, type="gender", value=gender)
            total = len(rec.movies.all())
            movies = rec.movies.all()[start: start + limit]
            serializer = MovieSerializer(movies, many=True)
            data = {"data": serializer.data,
                    "total": total, "start": start, "limit": limit, "value": gender}
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            # filter movies
            id = request.GET.get('id', request.GET.get('movie_id', None))
            title = request.GET.get('title', None)
            genres = request.GET.get("genres", None)
            if id:
                movies = movies.filter(pk=id)
            if title:
                movies = movies.filter(title__icontains=title)
            if genres:
                genres = genres.split(",")
                for genre in genres:
                    movies = movies.filter(genres__icontains=genre)

            # sort by ratings, views
            sort_ratings = request.GET.get("sort_ratings", None)
            sort_views = request.GET.get("sort_views", None)
            if sort_ratings:
                if sort_ratings == "1":
                    movies = movies.order_by("-avg_rating")
                else:
                    movies = movies.order_by("avg_rating")
            if sort_views:
                if sort_views == "1":
                    movies = movies.order_by("-rating_count")
                else:
                    movies = movies.order_by("rating_count")

            serializer = MovieSerializer(movies, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # username = request.data.get("username", None)
        # token = request.data.get("token", None)
        # user = User.objects.get(username=username)
        movies = request.data.get('movies', [])

        # if not user.is_staff or user.refresh_token != token:
        #     return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        #
        # response = verify_token(token)
        # if response.status_code != 200:
        #     response = refresh_token(token)
        #     if response.status_code == 200:
        #         new_token = json.loads(response.text)["token"]
        #         user.refresh_token = new_token

        #     if response and response.status_code == 200:
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)

            if not (id and title and genres):
                continue
            if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
                continue

            Movie(id=id, title=title, genres='|'.join(genres)).save()

        story = request.data.get("story", None)
        if story:
            for s in story:
                movie_id = s.get("movie_id", None)
                st = s.get("story", None)
                movie = get_object_or_404(Movie, id=movie_id)
                movie.story = st
                movie.save()

        return Response(status=status.HTTP_200_OK)
        # user.refresh_token = ""
        # user.save()
        # auth_logout(request)
        # return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        username = request.data.get("username", None)
        token = request.data.get("token", None)
        user = User.objects.get(username=username)

        if not user.is_staff:
            return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        if user.refresh_token != token:
            user.refresh_token = ""
            user.save()
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        response = verify_token(token)
        if response.status_code != 200:
            response = refresh_token(token)
            if response.status_code == 200:
                new_token = json.loads(response.text)["token"]
                user.refresh_token = new_token

        if response and response.status_code == 200:
            movie.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        user.refresh_token = ""
        user.save()
        return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    if request.method == 'PUT':
        username = request.data.get("username", None)
        token = request.data.get("token", None)
        user = User.objects.get(username=username)

        if not user.is_staff:
            return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        if user.refresh_token != token:
            user.refresh_token = ""
            user.save()
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        response = verify_token(token)
        if response.status_code != 200:
            response = refresh_token(token)
            if response.status_code == 200:
                new_token = json.loads(response.text)["token"]
                user.refresh_token = new_token

        if response and response.status_code == 200:
            movie_info = request.data.get("movie", None)

            if movie_info:
                movie.title = movie_info["title"]
                genres = movie_info["genres"]
                genres = '|'.join(genres)
                movie.genres = genres
                movie.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(data={"error": "입력값이 없습니다."}, status=status.HTTP_204_NO_CONTENT)

        user.refresh_token = ""
        user.save()
        return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(['GET', 'POST'])
def rating_list(request):

    if request.method == 'GET':
        raitings = Rating.objects.all()
        serializer = RatingSerializer(raitings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        # username = request.data.get("username", None)
        # token = request.data.get("token", None)
        # user = User.objects.get(username=username)
        #
        # if not user.is_staff or user.refresh_token != token:
        #     return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        #
        # response = verify_token(token)
        # if response.status_code != 200:
        #     response = refresh_token(token)
        #     if response.status_code == 200:
        #         new_token = json.loads(response.text)["token"]
        #         user.refresh_token = new_token

        #     if response and response.status_code == 200:

        for item in ratings:
            username = item.get('username', None)
            user = get_object_or_404(User, username=username)
            movie_id = item.get('movie_id', None)
            movie = get_object_or_404(Movie, id=movie_id)
            rating = item.get('rating', None)
            timestamp = item.get('timestamp', None)
            if not (movie_id and rating and timestamp):
                continue
            time = datetime.utcfromtimestamp(
                int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")
            Rating.objects.create(
                user=user, movie_id=movie_id, rating=rating, timestamp=time)
            movie.total_rating += int(rating)
            movie.rating_count += 1
            movie.avg_rating = round(
                movie.total_rating / movie.rating_count, 2)
            movie.save()
        return Response(status=status.HTTP_200_OK)
        # user.refresh_token = ""
        # user.save()
        # return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(['GET', 'PUT', 'DELETE'])
def rating_detail(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        # username = request.data.get("username", None)
        # token = request.data.get("token", None)
        # user = User.objects.get(username=username)
        #
        # if not user.is_staff or user.refresh_token != token:
        #     return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        #
        # response = verify_token(token)
        # if response.status_code != 200:
        #     response = refresh_token(token)
        #     if response.status_code == 200:
        #         new_token = json.loads(response.text)["token"]
        #         user.refresh_token = new_token

        #     if response and response.status_code == 200:
        rating.delete()
        return Response(status=status.HTTP_200_OK)
        # user.refresh_token = ""
        # user.save()
        # return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    if request.method == 'PUT':
        rating = request.data.get('rating', None)
        # username = request.data.get("username", None)
        # token = request.data.get("token", None)
        # user = User.objects.get(username=username)
        #
        # if not user.is_staff or user.refresh_token != token:
        #     return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        #
        # response = verify_token(token)
        # if response.status_code != 200:
        #     response = refresh_token(token)
        #     new_token = json.loads(response.text)["token"]
        #     user.refresh_token = new_token

        #     if response and response.status_code == 200:

        if rating:
            rating.rating = rating
            rating.timestamp = datetime.now()
            rating.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # user.refresh_token = ""
        # user.save()
        # return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(['GET'])
def movie_ratings(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        raitings = movie.ratings.all()
        serializer = RatingSerializer(raitings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def movie_followers(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = UserSerializer(movie.followers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        if request.user.is_authenticated:
            movie.followers.add(request.user)
            movie.save()
            serializer = UserSerializer(movie.followers, many=True)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def refresh_recommendations(request):
    age = [1, 18, 25, 35, 45, 50, 56]
    occupation = [
        "academic/educator",
        "artist",
        "clerical/admin",
        "college/grad student",
        "K-12 student",
        "customer service",
        "doctor/health care",
        "executive/managerial",
        "farmer",
        "homemaker",
        "lawyer",
        "programmer",
        "sales/marketing",
        "scientist",
        "self-employed",
        "technician/engineer",
        "tradesman/craftsman",
        "writer"
    ]
    gender = ["M", "F"]

    movies = Movie.objects.all()
    created = False

    for value in age:
        temp = movies.annotate(
            age_count=Count(
                'ratings', filter=Q(ratings__user__age=value))
        ).order_by('-age_count')[:100]
        rec, check = Recommendation.objects.get_or_create(
            type="age", value=value)
        created = check or created
        rec.movies.set(temp)
        rec.save()
    for value in occupation:
        temp = movies.annotate(
            occupation_count=Count(
                'ratings', filter=Q(ratings__user__occupation=value))
        ).order_by('-occupation_count')[:100]
        rec, check = Recommendation.objects.get_or_create(
            type="occupation", value=value)
        created = check or created
        rec.movies.set(temp)
        rec.save()
    for value in gender:
        temp = Movie.objects.annotate(
            gender_count=Count(
                'ratings', filter=Q(ratings__user__gender=value))
        ).order_by('-gender_count')[:100]
        rec, check = Recommendation.objects.get_or_create(
            type="gender", value=value)
        created = check or created
        rec.movies.set(temp)
        rec.save()
    if created:
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_202_ACCEPTED)

# 유사한 영화 추천 알고리즘 (영화 클러스터링)
@api_view(['POST'])
def related_movies(request):
    movie_id = request.data.get('movieId', None)
    username = request.data.get("username", None)
    token = request.data.get("token", None)
    name = request.data.get("name", None)

    print(request.data)
    if not movie_id:
        return Response(data={"error": "정보 없음"}, status=status.HTTP_400_BAD_REQUEST)

    movie = get_object_or_404(Movie, id=movie_id)
    if username:
        print(1)
        if username != name:
            return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        user = get_object_or_404(User, username=username)

        if not user.is_staff:
            return Response(data={"error": "권한 없음"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        if user.refresh_token != token:
            user.refresh_token = ""
            user.save()
            return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

        response = verify_token(token)
        if response.status_code != 200:
            response = refresh_token(token)
            if response.status_code == 200:
                new_token = json.loads(response.text)["token"]
                user.refresh_token = new_token

        if response and response.status_code == 200:
            related_movies = Movie.objects.filter(Q(cluster__exact=movie.cluster) & ~Q(
                ratings__user__username=username)).order_by("-avg_rating")[:10]
            serializer = MovieSerializer(related_movies, many=True)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

        user.refresh_token = ""
        user.save()
        auth_logout(request)
        return Response(data={"error": "token"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    related_movies = Movie.objects.filter(
        Q(cluster__exact=movie.cluster) & ~Q(ratings__user__username=username)).order_by("-avg_rating")[:10]
    serializer = MovieSerializer(related_movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
