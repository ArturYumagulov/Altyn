import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from users.decorators.decorators import json_login_required


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
    if request.method == "POST":
        return JsonResponse(request.body)
    else:
        return JsonResponse({'result': 'error'})
