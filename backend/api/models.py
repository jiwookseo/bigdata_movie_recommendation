from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)

    def str(self):
        return "{}: {}".format(self.id, self.user.username)

    @property
    def rating_cnt(self):
        return len(self.user.ratings.all())


#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    avg_rating = models.FloatField(default=0)
    total_rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    story = models.TextField()

    @property
    def genres_array(self):
        return self.genres.split('|')

    def str(self):
        return "{}: {}({})".format(self.id, self.title, self.genres)


class Rating(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="ratings")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)
