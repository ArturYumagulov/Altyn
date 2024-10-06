from django.urls import path

from . import views


urlpatterns = [
    path('main/', views.movie_main, name="movie_main"),
    path('movies/', views.movies, name="movies"),
    path('get-filters/', views.get_json_filters, name='get_filter'),
    path('search/', views.movie_search, name='movie_search'),
    path('detail/<slug:slug>', views.movie_detail, name='movie_detail'),
]