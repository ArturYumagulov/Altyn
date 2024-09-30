from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import views_json, views_http


urlpatterns = [
    # ----------REGISTER--------
    path("login/", views_json.user_login, name="login"),
    path("logout/", views_json.user_logout, name="logout"),
    path("register/", views_json.user_register, name="register"),
    path("valid-data/", views_json.valid_data, name="users_valid_data"),
    path(
        "change-password/",
        views_http.change_password, name="change_password"
    ),
    path(
        "password-change/done/",
        views_json.change_pass_email, name="change_password_done"
    ),
    path(
        "password-reset-form/<token>/",
        views_http.reset_pass_form, name="reset_password_form"
    ),
    path(
        "password-reset/",
        views_json.reset_password, name="reset_password"
    ),
    path("res-login-page/", views_http.res_login_page, name="res_login_page"),
    # path('res-login/', views_http.res_user_login, name='res_login'),
    path("verify/<token>/", views_http.verify_email, name="verify_email"),
    #  --------- PROFILE ---------------------
    path("profile/", views_http.profile, name="profile"),
    path("edit-profile/", views_http.edit_profile, name="edit_profile"),

    path("index/", views_json.index, name="index"),
    path('edit-email-phone/', views_json.profile_valid_email, name="edit_email_phone"),
    path('edit-user-profile/', views_json.edit_user_profile, name="edit_user_profile"),
    path('email-verify/', views_json.email_edit_code_gen, name="email-verify"),
    path('verify-code/', views_json.verify_code, name='verify_code')
]
