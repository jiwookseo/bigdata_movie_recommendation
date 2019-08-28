from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Profile, Rating
from django.contrib.auth.models import User
from api.serializers import MovieSerializer, DetailMovieSerializer
from rest_framework.response import Response
from datetime import datetime


@api_view(['GET', 'POST', 'DELETE'])
def movies(request):

    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie_id', None))
        title = request.GET.get('title', None)
        genres = request.GET.get("genres", None)
        age = request.GET.get("age", None)

        sort_ratings = request.GET.get("sort_ratings", None)
        sort_views = request.GET.get("sort_views", None)

        movies = Movie.objects.all()

        if id:
            movies = movies.filter(pk=id)
        if title:
            movies = movies.filter(title__icontains=title)
        if genres:
            genres = genres.split(",")
            for genre in genres:
                movies = movies.filter(genres__icontains=genre)
        if age:
            users = Profile.objects.all().filter(age=age)
            movie_set = {"movies": set()}
            for user in users:
                for rating in user.ratings.all():
                    movie_set["movies"].add(rating.movie.title)
            return Response(data=movie_set["movies"], status=status.HTTP_200_OK)


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

        if id or (title and len(movies) == 1):
            serializer = DetailMovieSerializer(movies, many=True)
        else:
            serializer = MovieSerializer(movies, many=True)


        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        movies = request.data.get('movies', None)

        if movies != None:
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
        if story != None:
            i = 0
            for s in story:
                movie_id = s.get("movie_id", None)
                st = s.get("story", None)

                movie = Movie.objects.get(id=movie_id)
                movie.story = st
                movie.save()
                i += 1
                print(i)


        ratings = request.data.get('ratings', None)
        if ratings != None:
            i = 0
            for r in ratings:
                user_id = r.get('user_id', None)
                movie_id = r.get('movie_id', None)
                rating = r.get('rating', None)
                timestamp = r.get("timestamp", None)
                time = datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")

                user = User.objects.get(id=user_id)
                profile = Profile.objects.get(user=user)
                movie = Movie.objects.get(id=movie_id)

                r = Rating()
                r.user = profile
                r.movie = movie
                r.timestamp = time
                r.rating = rating
                r.save()

                movie.avg_rating = round((movie.avg_rating * movie.rating_count + int(rating)) / (movie.rating_count + 1), 5)
                movie.rating_count += 1
                movie.save()

                i += 1
                print(i)

        return Response(status=status.HTTP_200_OK)