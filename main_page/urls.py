from django.urls import path

from main_page.views import index

urlpatterns = [
    path('', index, name='main')
]