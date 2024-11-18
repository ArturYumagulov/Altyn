from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='regions'),
    path('get-region-resources/', views.get_region_resources, name='get_resources'),
    path('screen-points/<slug:slug>', views.screenpoint_detail, name='screenpoint_detail'),
]