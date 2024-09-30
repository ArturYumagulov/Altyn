from django.urls import path

from . import views


urlpatterns = [
    path('main/', views.movie_main, name="movie_main"),
    # path('create-app/', views.create_app, name="create_app")
]