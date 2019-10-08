from django.db import models
from accounts.models import User
from api.models import Movie


'''
유저 별 맞춤 추천 영화 () + 해당 영화에 대한 유저의 예상 평점
추천 영화 리스트는 각 알고리즘 별로 최대 5개. 
알고리즘은 KNN (User Based, Movie Based), MF(적용 예정) 등을 사용
'''

class RecommendedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rcmd_movies")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    exp_rating = models.FloatField(default=0)
