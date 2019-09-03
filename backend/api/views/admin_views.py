# Python Modules
from datetime import datetime

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from api.models import Movie, Rating
from accounts.models import User

# Serializer
from accounts.serializers import UserSerializer
from api.serializers import MovieSerializer, RatingSerializer

# etc
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404




# Movie
@api_view(['GET'])
def movies(request):
    try:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST', 'PUT', 'DELETE'])
def movie(request):
    pass



# User
@api_view(['GET'])
def users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'PUT', 'DELETE'])
def user(request):
    pass
