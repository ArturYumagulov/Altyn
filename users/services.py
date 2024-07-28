from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

User = get_user_model()


def send_email_for_verify(request, email, token):

    current_site = get_current_site(request).domain
    context = {
        'email': email,
        'domain': current_site,
        'token': token
    }
    message = render_to_string(
        "users/verify_email.html",
        context=context,
    )
    send_mail(
        "Подтверждение подписки",
        message,
        settings.RECIPIENTS_EMAIL,
        [email],
        fail_silently=False
    )


def create_look_user(request, user_data):
    user = User.objects.create_user(
        username=user_data.get('email'),
        email=user_data.get('email'),
        phone=user_data.get('phone'),
        password=user_data.get('password'),
    )
    send_email_for_verify(request, user.email, user.verify_token)
    return user
