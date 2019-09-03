from django.contrib import admin
from api.models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    actions = ['km_clustering', 'hr_clustering', 'em_clustering']
    list_display = ['title', 'genres', 'avg_rating', 'rating_count', 'cluster']
    list_display_links = ['title']
    list_per_page = 50

    def km_clustering(self, request, queryset):
        self.message_user(request, 'K-Means 클러스터링 수행')
    km_clustering.short_description = 'K-Means Clustering'

    def hr_clustering(self, request, queryset):
        self.message_user(request, 'HR 클러스터링 수행')
    hr_clustering.short_description = 'HR Clustering'

    def em_clustering(self, request, queryset):
        self.message_user(request, 'EM 클러스터링 수행')
    em_clustering.short_description = "EM Clustering"



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
