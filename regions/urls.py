from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='regions'),
    path('get-region-resources/', views.get_region_resources, name='get_resources'),
    path('detail/<str:resource_type>/<slug:slug>/', views.resources_detail, name='resource_detail'),
    # path('screen-points/<slug:slug>', views.screenpoint_detail, name='screenpoint_detail'),
    # path('internet-resources/<slug:slug>', views.internet_resources_detail, name='internet_resources_detail'),

]