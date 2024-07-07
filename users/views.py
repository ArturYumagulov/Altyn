import json

from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required

from users.forms import LoginForm


# Create your views here.

@csrf_exempt
def user_login(request):
    email = json.loads(request.body).get('email')
    password = json.loads(request.body).get('password')
    if request.method == 'POST':
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'result': 'ok'}, safe=False)
            else:
                return JsonResponse({'result': 'no_active'}, safe=False)
        else:
            return JsonResponse({'result': 'no_register'}, safe=False)