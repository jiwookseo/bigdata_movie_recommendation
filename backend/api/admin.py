from django.contrib import admin
from api.models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    actions = ['km_clustering', 'hr_clustering', 'em_clustering']
    list_display = ['title', 'genres', 'avg_rating', 'rating_count', 'cluster']
    list_display_links = ['title']
    list_per_page = 50


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating', 'timestamp']
    list_per_page = 50

    def user(self, rating):
        return rating.user.username
    user.short_description = 'User'

    def movie(self, rating):
        return rating.movie.title
    movie.short_description = 'Movie'
