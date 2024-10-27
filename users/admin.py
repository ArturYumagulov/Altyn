from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from .models import CustomUser
from .services import send_email_for_verify


# from movies.models import Playlist

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = [
        "pk",
        "username",
        "phone",
        "email",
        "is_active",
        "is_looking",
        "is_shooting",
        "is_show",
        "is_organize",
    ]
    list_display_links = ["pk", "email", "username"]
    list_filter = ["is_staff", 'is_active', 'date_joined']
    fieldsets = (
        (None, {"fields": ("username",)}),
        (
            "Персональная информация",
            {
                "fields": (
                    "avatar",
                    "first_name",
                    "last_name",
                    "surname",
                    "birthday",
                    "phone",
                    "email",
                    "male",
                    "password",
                    "site",
                    "platform_name",
                    "company_name",
                    "social_networks",
                    "roles",
                    "region",
                    "location",
                    "verify_token",
                    "date_joined",
                )
            },
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_looking",
                    "is_show",
                    "is_shooting",
                    "is_organize",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Важные даты", {"fields": ("last_login",)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "phone", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["-date_joined"]
    readonly_fields = ("get_avatar", "verify_token", "date_joined")

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width=70')

    get_avatar.short_description = "Аватар"

    @admin.action(description="Отправить письмо для подтверждения")
    def send_verify_button(self, request, queryset):
        if len(queryset) == 0:
            send = send_email_for_verify(request, queryset[0].email, queryset[0].verify_token)
            if send.get('result'):
                self.message_user(request, send.get('message'), level='info')
            else:
                self.message_user(request, send.get('message'), level='error')
        else:
            for user in queryset:
                # Логика для отправки письма
                send = send_email_for_verify(request, user.email, user.verify_token)
                if send.get('result'):
                    self.message_user(request, send.get('message'), level='info')
                else:
                    self.message_user(request, send.get('message'), level='error')
    actions = [send_verify_button]


admin.site.register(CustomUser, UserAdmin)
