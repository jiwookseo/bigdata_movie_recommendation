from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating_cnt = serializers.ReadOnlyField()
    image = serializers.SerializerMethodField('get_image')
    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender',
                  'age', 'occupation', 'rating_cnt', 'image', 'thumbnail', 'subscribe')

    def get_image(self, obj):
        return 'http://localhost:8000' + obj.image.url if obj.image else None

    def get_thumbnail(self, obj):
        return 'http://localhost:8000' + obj.thumbnail.url if obj.image else None
