from .models import Profile, Movie, Rating
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    rating_cnt = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender',
                  'age', 'occupation', 'rating_cnt')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff


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
        fields = ('id', 'rating', 'username',
                  'movie_title', 'movie_id', 'timestamp')

    def get_username(self, obj):
        return obj.user.user.username

    def get_movie_title(self, obj):
        return obj.movie.title
