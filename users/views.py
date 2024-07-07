import json

from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required


# Create your views here.

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


def user_logout(request):
    logout(request)
    return JsonResponse({'result': 'logout'})
