from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating
from accounts.models import User
from api.serializers import MovieSerializer, RatingSerializer
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def movie_list(request):

    if request.method == 'GET':
        # recommend by age, occupation, gender
        age = request.GET.get("age", None)
        occupation = request.GET.get("occupation", None)
        gender = request.GET.get("gender", None)
        if age:
            movies = Movie.objects.annotate(
                age_count=Count(
                    'ratings', filter=Q(ratings__user__age=age))
            ).order_by('-age_count')
            serializer = MovieSerializer(movies, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif occupation:
            movies = Movie.objects.annotate(
                occupation_count=Count(
                    'ratings', filter=Q(ratings__user__occupation=occupation))
            ).order_by('-occupation_count')
            serializer = MovieSerializer(movies, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif gender:
            movies = Movie.objects.annotate(
                gender_count=Count(
                    'ratings', filter=Q(ratings__user__gender=gender))
            ).order_by('-gender_count')
            serializer = MovieSerializer(movies, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            movies = Movie.objects.all()

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
        movies = request.data.get('movies', [])
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


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'PUT':
        title = movie.get('title', None)
        genres = movie.get('genres', None)
        if not (title and genres):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if title:
            movie.title = title
        if genres:
            movie.genres = '|'.join(genres)
        movie.save()
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def rating_list(request):

    if request.method == 'GET':
        raitings = Rating.objects.all()
        serializer = RatingSerializer(raitings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)

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

@api_view(['GET', 'PUT', 'DELETE'])
def rating_detail(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

@api_view(['GET', 'PUT', 'DELETE'])
def rating_detail(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)

    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        rating.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'PUT':
        rating = request.data.get('rating', None)
        if rating:
            rating.rating = rating
            rating.timestamp = datetime.now()
            rating.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def movie_ratings(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        raitings = movie.ratings.all()
        serializer = RatingSerializer(raitings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
