import json

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from users.decorators.decorators import json_login_required
from users.services import create_look_user

User = get_user_model()


def user_login(request):
    email = json.loads(request.body).get('email')
    password = json.loads(request.body).get('password')
    if request.method == 'POST':
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'result': 'login', 'user': user.username}, safe=False)
            else:
                return JsonResponse({'result': 'no_active', 'user': user.username}, safe=False)
        else:
            return JsonResponse({'result': 'no_register'}, safe=False)


@login_required
def index(request):
    return JsonResponse({'content': True}, safe=False)


def user_logout(request):
    logout(request)
    return JsonResponse({'detail': 'True'})


def user_register(request):
    """Регистрация"""

    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        if data.get('type') == 'is_looking' or data.get('type') == 'is_shooting':
            create_look_user(data)
            return JsonResponse({'result': True}, safe=False)

    return JsonResponse({'result': 'error'}, safe=False)


def valid_data(request):
    """Валидация данных при регистрации"""
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        if data.get('type') == 'email':
            try:
                print(User.objects.get(email=data.get('value')))
                return JsonResponse({'result': True, 'text': "Данный email уже зарегистрирован"}, safe=False)
            except User.DoesNotExist:
                return JsonResponse({'result': False}, safe=False)

        return JsonResponse({'result': False}, safe=False)
    return JsonResponse({'result': False}, safe=False)



