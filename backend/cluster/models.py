from django.db import models
from accounts.models import User
from api.models import Movie




# Similarity
# former는 latter보다 앞선 id를 갖고 있는 데이터이다.

class MovieSimilarity(models.Model):
    movie_former = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="similar_movies_latter")
    movie_latter = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="similar_movies_former")
    similarity = models.FloatField()


class UserSimilarity(models.Model):
    user_former = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="similar_users_latter")
    user_latter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="similar_users_former")
    similarity = models.FloatField()

