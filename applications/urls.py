from django.urls import path

from . import views


urlpatterns = [
    path('app/', views.altyn_app, name="altyn_app"),
    path('create-app/', views.create_altyn_app, name="create_altyn_app"),
    path('send-doc/', views.send_docx)
]