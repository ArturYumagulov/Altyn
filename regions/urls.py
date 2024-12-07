from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='regions'),
    path('get-region-resources/', views.get_region_resources, name='get_resources'),
    path('detail/<str:resource_type>/<slug:slug>/', views.resources_detail, name='resource_detail'),
    path('portrait-detail/<int:pk>/', views.portrait_detail, name='portrait_detail'),
    path('location-detail/<int:pk>/', views.location_detail, name='location_detail')

]