from django.urls import path
from .views import views_json, views_http


urlpatterns = [
    path('login/', views_json.user_login, name='login'),
    path('logout/', views_json.user_logout, name='logout'),
    path('register/', views_json.user_register, name='register'),
    path('valid-data/', views_json.valid_data, name='users_valid_data'),

    # --------------------------------------------------
    path('res-login-page/', views_http.res_login_page, name='res_login_page'),
    # path('res-login/', views_http.res_user_login, name='res_login'),
    path('index/', views_json.index, name='index')

]