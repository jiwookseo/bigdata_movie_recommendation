from .models import Profile, Movie
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    gender = serializers.SerializerMethodField("get_gender")
    age = serializers.SerializerMethodField("get_age")
    occupation = serializers.SerializerMethodField("get_occupation")

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation')

    def get_gender(self, obj):
        return obj.profile.gender

    def get_age(self, obj):
        return obj.profile.age

    def get_occupation(self, obj):
        return obj.profile.occupation


class DetailProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    gender = serializers.SerializerMethodField("get_gender")
    age = serializers.SerializerMethodField("get_age")
    occupation = serializers.SerializerMethodField("get_occupation")
    ratings = serializers.SerializerMethodField("get_ratings")

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation', "ratings")

    def get_gender(self, obj):
        return obj.profile.gender

    def get_age(self, obj):
        return obj.profile.age

    def get_occupation(self, obj):
        return obj.profile.occupation

    def get_ratings(self, obj):
        array = []
        for rating in obj.profile.ratings.all():
            array.append(rating.movie.title)
        return array


class OptionalProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    # username = serializers.SerializerMethodField("get_username")
    ratings = serializers.SerializerMethodField("get_ratings")

    class Meta:
        model = Profile
        fields = ("id", "age", "ratings")

    def get_username(self, obj):
        return obj.user.username

    def get_ratings(self, obj):
        array = []
        for rating in obj.ratings.all():
            array.append(rating.movie.title)
        return array


class MovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    avg_rating = serializers.SerializerMethodField("get_avg_rating")

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', "avg_rating", "rating_count")

    def get_avg_rating(self, obj):
        return round(obj.avg_rating, 2)


class DetailMovieSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()
    avg_rating = serializers.SerializerMethodField("get_avg_rating")
    ratings = serializers.SerializerMethodField("get_ratings")

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', "avg_rating", "rating_count", "ratings", "story")

    def get_avg_rating(self, obj):
        return round(obj.avg_rating, 2)

    def get_ratings(self, obj):
        array = []
        for rating in obj.ratings.all():
            array.append(rating.user.user.username)
        return array
