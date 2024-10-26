import random
import secrets
import redis

from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from smtplib import SMTPDataError
import logging
from django.conf import settings

User = get_user_model()


def send_email_for_verify(request, email, token):

    current_site = get_current_site(request).domain
    context = {"email": email, "domain": current_site, "token": token}
    message = render_to_string(
        "users/email/verify_email.html",
        context=context,
    )
    try:
        send_mail(
            "Подтверждение подписки",
            message,
            settings.RECIPIENTS_EMAIL,
            [email],
            fail_silently=False,
        )
        return {'result': True, 'message': f"Письмо с подтверждением на {email} отправлено"}

    except SMTPDataError as e:
        # logger.error(f"SMTPDataError: {e.smtp_code} - {e.smtp_error.decode('utf-8')}")
        print("Ошибка отправки письма, проверьте настройки SMTP и повторите попытку.")

        return {
            'result': False,
            'message': f"Произошла ошибка при отправке письма. проверьте настройки SMTP. {e}"
        }

    except Exception as e:
        # logger.error(f"Произошла ошибка: {e}")
        print(f"Произошла ошибка при отправке письма. {e}")
        return {
            'result': False,
            'message': f"Произошла ошибка при отправке письма. {e}"
        }



def send_email_for_reset_pass(request, email, token):

    current_site = get_current_site(request).domain
    context = {"email": email, "domain": current_site, "token": token}
    message = render_to_string(
        "users/email/reset_pass_verify_email.html",
        context=context,
    )
    send_mail(
        'Сброс пароля на сайте "Алтын-телинке"',
        message,
        settings.RECIPIENTS_EMAIL,
        [email],
        fail_silently=False,
    )


def create_look_user(request, user_data):
    user = User.objects.create_user(
        username=user_data.get("email"),
        email=user_data.get("email"),
        phone=user_data.get("phone"),
        password=user_data.get("password"),
    )
    return user


def send_email(username, email, code):
    subject = f'"Алтын-телинке" - Верификация электронного адреса"'
    domain = settings.SITE_URL
    message = f"""
    Здравствуйте, {username}!
    Мы получили запрос на отправку разового кода для изменения электронного адреса.

    Ваш разовый код: {code}

    Если вы не запрашивали этот код, можете смело игнорировать это сообщение электронной почты. Возможно, кто-то ввел ваш адрес электронной почты по ошибке.

    С уважением. Сайт кинопремии "Алтын-телинке"
    {domain}
    """

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


def confirm_code_generator(email, username):
    r = redis.Redis(host='localhost')
    random_number = random.randint(0, 999999)
    if r.set(email, random_number):
        send_email(username, email, random_number)
        r.expire(email, 86400)
        return True
    return False


def valid_code(code, email):
    r = redis.Redis(host='localhost', decode_responses=True)
    if r.get(email) == str(code):
        return True
    return False
