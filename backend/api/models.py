from django.db import models
from accounts.models import User
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    avg_rating = models.FloatField(default=0)
    total_rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    story = models.TextField()
    cluster = models.IntegerField(null=True)
    poster = models.URLField(default="")
    still_cut = models.URLField(default="")
    followers = models.ManyToManyField(
        User, related_name="followings")

    @property
    def genres_array(self):
        return self.genres.split('|')

    def str(self):
        return "{}: {}({})".format(self.id, self.title, self.genres)


class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ratings")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)


class Recommendation(models.Model):
    type = models.CharField(max_length=50, default="")
    value = models.CharField(max_length=50, default="")
    movies = models.ManyToManyField(Movie, related_name="recommendations")
