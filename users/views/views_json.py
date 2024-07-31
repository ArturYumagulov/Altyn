import json
import secrets

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from users.decorators.decorators import json_login_required
from users.services import create_look_user, send_email_for_verify, send_email_for_reset_pass

User = get_user_model()


def user_login(request):
    email = json.loads(request.body).get("email")
    password = json.loads(request.body).get("password")
    print(request.body)
    if request.method == "POST":
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse(
                    {"result": "login", "user": user.username}, safe=False
                )
            else:
                send_email_for_verify(request, user.email, user.verify_token)
                return JsonResponse(
                    {"result": "no_active", "user": user.username}, safe=False
                )
        else:
            return JsonResponse({"result": "no_register"}, safe=False)


@login_required
def index(request):
    return JsonResponse({"content": True}, safe=False)


def user_logout(request):
    logout(request)
    return JsonResponse({"detail": "True"})


def user_register(request):
    """Регистрация"""

    if request.method == "POST":
        data = json.loads(request.body)
        if data.get("type") == "is_looking":
            new_user = create_look_user(request, data)
            new_user.is_looking = True
            new_user.save()
            send_email_for_verify(request, new_user.email, new_user.verify_token)
            return JsonResponse({"result": True}, safe=False)
        elif data.get("type") == "is_shooting":
            new_user = create_look_user(request, data)
            new_user.is_shooting = True
            new_user.save()
            send_email_for_verify(request, new_user.email, new_user.verify_token)
            return JsonResponse({"result": True}, safe=False)
        elif data.get("type") == "is_show":
            new_user = create_look_user(request, data)
            new_user.is_show = True
            new_user.last_name = data.get("lastname")
            new_user.first_name = data.get("firstname")
            new_user.surname = data.get("surname")
            new_user.company_name = data.get("companyName")
            new_user.site = data.get("site")
            new_user.save()
            send_email_for_verify(request, new_user.email, new_user.verify_token)
            return JsonResponse({"result": True}, safe=False)
        elif data.get("type") == "is_organize":
            new_user = create_look_user(request, data)
            new_user.is_organize = True
            new_user.last_name = data.get("lastname")
            new_user.first_name = data.get("firstname")
            new_user.surname = data.get("surname")
            new_user.platform_name = data.get("platformName")
            new_user.site = data.get("site")
            new_user.save()
            send_email_for_verify(request, new_user.email, new_user.verify_token)
            return JsonResponse({"result": True}, safe=False)

    return JsonResponse({"result": "error"}, safe=False)


def valid_data(request):
    """Валидация данных при регистрации"""
    if request.method == "POST":
        email_exists = User.objects.filter(
            email=json.loads(request.body).get("email")
        ).exists()
        phone_exists = User.objects.filter(
            phone=json.loads(request.body).get("phone")
        ).exists()
        return JsonResponse(
            {"emailExists": email_exists, "phoneExists": phone_exists}, safe=False
        )
    return JsonResponse({"result": False}, safe=False)


def change_pass_email(request):
    if request.method == 'POST':
        user = User.objects.get(email=json.loads(request.body).get('email'))
        send_email_for_reset_pass(request, user.email, user.verify_token)
        return JsonResponse({'result': True}, safe=False)
    return JsonResponse({'result': False}, safe=False)


def reset_password(request):

    if request.method == "POST":
        data = json.loads(request.body)
        try:
            user = User.objects.get(verify_token=data.get('token'))
            user.set_password(data.get('password'))
            user.save()
            return JsonResponse({'result': True}, safe=False)
        except User.DoesNotExist:
            return JsonResponse({'result': False}, safe=False)

    return JsonResponse({'result': False}, safe=False)


