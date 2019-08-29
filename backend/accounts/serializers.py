from accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    rating_cnt = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation', 'rating_cnt')