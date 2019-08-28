# django
from django.shortcuts import get_object_or_404

# rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from django.contrib.auth.models import User
from api.models import Movie, Profile, Rating


# Clustering 및 Data 저장하기
# Clustering된 데이터를 가져오는 것은 모델별 views에서 실행

