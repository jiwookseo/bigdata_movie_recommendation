from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Profile
# from api.serializers import RatingSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from datetime import datetime


@api_view(['GET', 'POST', 'DELETE'])
def rating(request):

    # if request.method == 'GET':
    #     id = request.GET.get('id', request.GET.get('rating_id', None))
    #     user_id = request.GET.get("user_id", None)
    #     movie_id = request.GET.get('movie_id', None)
    #     rating = request.GET.get("rating", None)
    #
    #     ratings = Rating.objects.all()
    #
    #     if id:
    #         ratings = ratings.filter(id=id)
    #     if user_id:
    #         ratings = ratings.filter(user=user_id)
    #     if movie_id:
    #         ratings = ratings.filter(movie=movie_id)
    #     if rating:
    #         ratings = ratings.filter(rating=rating)
    #
    #     serializer = RatingSerializer(ratings, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)


    # if request.method == 'DELETE':
    #     rating = Rating.objects.all()
    #     rating.delete()
    #     return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for r in ratings:
            user_id = r.get('user_id', None)
            movie_id = r.get('movie_id', None)
            rating = r.get('rating', None)
            timestamp = r.get("timestamp", None)
            time = datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")

            user = User.objects.get(id=user_id)
            profile = Profile.objects.get(user=user)

            movie = Movie.objects.get(id=movie_id)
            movie.rating = rating
            movie.avg_rating = round((movie.avg_rating * movie.rating_count + int(rating)) / (movie.rating_count + 1), 5)
            movie.rating_count += 1
            movie.timestamp = time
            movie.save()

            movie.user.add(profile)
            print(movie.user)


        return Response(status=status.HTTP_200_OK)
