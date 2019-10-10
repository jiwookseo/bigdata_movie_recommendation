from accounts.models import User
from rest_framework import serializers
import os

NODE_ENV = os.environ.get("NODE_ENV", "develop")
BASE_URL = "http://52.78.81.59:8000" if NODE_ENV == "production" else "http://localhost:8000"


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating_cnt = serializers.ReadOnlyField()
    image = serializers.SerializerMethodField('get_image')
    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender',
                  'age', 'occupation', 'rating_cnt', 'image', 'thumbnail', 'subscribe', 'subscribe_at')

    def get_image(self, obj):
        return BASE_URL + obj.image.url if obj.image else None

    def get_thumbnail(self, obj):
        return BASE_URL + obj.thumbnail.url if obj.image else None
