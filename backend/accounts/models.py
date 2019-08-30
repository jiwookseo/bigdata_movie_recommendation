from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)
    cluster = models.IntegerField(null=True)
    refresh_token = models.TextField(default="")

    def __str__(self):
        return "{}".format(self.username)

    @property
    def rating_cnt(self):
        return len(self.ratings.all())