from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie
# from api.serializers import RatingSerializer
from accounts.models import User
from rest_framework.response import Response
from datetime import datetime


@api_view(['GET', 'POST', 'DELETE'])
def rating(request):

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for r in ratings:
            user_id = r.get('user_id', None)
            movie_id = r.get('movie_id', None)
            rating = r.get('rating', None)
            timestamp = r.get("timestamp", None)
            time = datetime.utcfromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")

            user = User.objects.get(id=user_id)

            movie = Movie.objects.get(id=movie_id)
            movie.rating = rating
            movie.avg_rating = round((movie.avg_rating * movie.rating_count + int(rating)) / (movie.rating_count + 1), 5)
            movie.rating_count += 1
            movie.timestamp = time
            movie.save()

            movie.user.add(user)


        return Response(status=status.HTTP_200_OK)
