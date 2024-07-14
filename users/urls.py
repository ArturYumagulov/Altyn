from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login_json, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('index/', views.index, name='index')
    path('res-login/', views.res_login, name='res_login')
]