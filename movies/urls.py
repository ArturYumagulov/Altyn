from django.urls import path

from . import views


urlpatterns = [
    path('app/', views.app, name="application"),
    path('create-app/', views.create_app, name="create_app")
]