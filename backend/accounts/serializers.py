from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating_cnt = serializers.ReadOnlyField()
    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender',
                  'age', 'occupation', 'rating_cnt', 'image', 'thumbnail', 'subscribe')

    def get_thumbnail(self, obj):
        return obj.thumbnail.url if obj.image else None
