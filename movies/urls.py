from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('main/', views.movie_main, name="movie_main"),
    path('movies/', views.movies, name="movies"),
    path('get-filters/', views.get_json_filters, name='get_filter'),
    path('search/', views.movie_search, name='movie_search'),
    path('detail/<slug:slug>', views.movie_detail, name='movie_detail'),
    path('get_star/', csrf_exempt(views.get_star_rating), name='get_star'),
    path('get_rating/<slug:slug>/', csrf_exempt(views.get_average_rating), name='get_rating'),
    path('valid_ip', csrf_exempt(views.valid_user_ip), name='ip_valid'),
]