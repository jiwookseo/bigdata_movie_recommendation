from .models import Movie, Rating, Recommendation
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array',
                  'avg_rating', 'rating_count', 'story', 'still_cut', 'poster')


class RatingSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    user_image = serializers.SerializerMethodField('get_user_image')
    user_thumbnail = serializers.SerializerMethodField('get_user_thumbnail')
    title = serializers.SerializerMethodField('get_movie_title')
    story = serializers.SerializerMethodField('get_movie_story')
    poster = serializers.SerializerMethodField('get_movie_poster')
    avg_rating = serializers.SerializerMethodField('get_avg_rating')
    genres = serializers.SerializerMethodField('get_genres')
    rating_id = serializers.SerializerMethodField("rename_id")
    id = serializers.SerializerMethodField("rename_movie")

    class Meta:
        model = Rating
        fields = ('rating_id', 'rating', 'avg_rating', 'username', 'user_image', 'user_thumbnail',
                  'title', 'id', 'story', 'poster', 'timestamp', 'genres')

    def get_movie_title(self, obj):
        return obj.movie.title

    def get_movie_poster(self, obj):
        return obj.movie.poster

    def get_movie_story(self, obj):
        return obj.movie.story

    def get_username(self, obj):
        return obj.user.username

    def get_user_image(self, obj):
        return 'http://localhost:8000' + obj.user.image.url if obj.user.image else None

    def get_user_thumbnail(self, obj):
        return 'http://localhost:8000' + obj.user.thumbnail.url if obj.user.image else None

    def get_avg_rating(self, obj):
        return obj.movie.avg_rating

    def get_genres(self, obj):
        return obj.movie.genres_array

    def rename_id(self, obj):
        return obj.id

    def rename_movie(self, obj):
        return obj.movie.id

        
class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('id', 'type', 'value')
