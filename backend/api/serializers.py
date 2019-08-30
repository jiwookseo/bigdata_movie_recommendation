from .models import Movie, Rating
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array',
                  'avg_rating', 'rating_count', 'story')


class RatingSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    movie_title = serializers.SerializerMethodField('get_movie_title')

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'username', 'movie_title', 'movie_id', 'timestamp')

    def get_movie_title(self, obj):
        return obj.movie.title

    def get_username(self, obj):
        print(obj.user.username)
        return obj.user.username
