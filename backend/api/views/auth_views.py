# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from api.models import create_profile, Profile
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from api.serializers import ProfileSerializer, RatingSerializer
#
#
# @api_view(['GET', 'POST'])
# def user_list(request):
#     if request.method == "GET":
#         username = request.GET.get(
#             'username', request.GET.get('username', None))
#         profiles = Profile.objects.all()
#         if username:
#             profiles = profiles.filter(user__username__icontains=username)
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         profiles = request.data.get('profiles', None)
#         for profile in profiles:
#             username = profile.get('username', None)
#             password = profile.get('password', None)
#             age = profile.get('age', None)
#             occupation = profile.get('occupation', None)
#             gender = profile.get('gender', None)
#
#             create_profile(username=username, password=password, age=age,
#                            occupation=occupation, gender=gender)
#         return Response(status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET'])
# def user_detail(request, username):  # 유저 정보 수정 하려면 PUT 만들어야함
#     profile = get_object_or_404(Profile, user__username=username)
#     serializer = ProfileSerializer(profile)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def user_ratings(request, username):
#     user = get_object_or_404(User, username=username)
#     serializer = RatingSerializer(user.profile.ratings, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
