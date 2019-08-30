from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating_cnt = serializers.ReadOnlyField()
    ratings = serializers.SerializerMethodField("get_movies")

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender',
                  'age', 'occupation', 'rating_cnt', "ratings")

    def get_movies(self, obj):
        arr = []
        for rating in obj.ratings.all():
            arr.append(rating.movie.title)
        return arr
