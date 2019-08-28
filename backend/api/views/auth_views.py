from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Profile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from api.serializers import ProfileSerializer, DetailProfileSerializer, OptionalProfileSerializer


@api_view(["GET", 'POST'])
def signup_many(request):

    if request.method == "GET":
        id = request.GET.get('id', request.GET.get('user_id', None))
        username = request.GET.get('username', None)
        age = request.GET.get("age", None)

        users = User.objects.all()

        if id:
            users = users.filter(pk=id)
        if username:
            users = users.filter(username=username)
        if age:
            users = Profile.objects.all()
            users = users.filter(age=age)


        if not id and not username and not age:
            serializer = ProfileSerializer(users, many=True)
        elif age:
            serializer = OptionalProfileSerializer(users, many=True)
        else:
            serializer = DetailProfileSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        i = 0
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)


            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)
            i += 1
            print(i)
        return Response(status=status.HTTP_201_CREATED)
