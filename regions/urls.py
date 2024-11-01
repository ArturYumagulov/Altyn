from django.urls import path

from .views import main, get_region_resources

urlpatterns = [
    path('', main, name='regions'),
    path('get-region-resources/', get_region_resources, name='get_resources')

]