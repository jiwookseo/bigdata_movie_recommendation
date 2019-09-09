from django.db import models
from accounts.models import User
from api.models import Movie


# 예상 평점
# 'Ex'pected Rating by 'M'ovie 'B'ased / 'U'ser 'B'ased

class ExpectedRating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ex_ratings")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="ex_ratings")
    ex_rating_mb = models.FloatField(default=0)
    ex_rating_ub = models.FloatField(default=0)
