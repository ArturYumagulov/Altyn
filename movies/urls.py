from django.urls import path

from . import views


urlpatterns = [
    path('main/', views.movie_main, name="movie_main"),
    path('all-movies/', views.all_movies, name="all_movies"),
    path('get-filters/', views.get_json_filters, name='get_filter'),
    path('search/', views.movie_search, name='movie_search')
]