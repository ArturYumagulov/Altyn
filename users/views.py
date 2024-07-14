import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from users.forms import LoginForm


# from django.contrib.auth.decorators import login_required


# Create your views here.

def json_login_required(view_func):
    def wrapper(requests, *args, **kwargs):
        if not requests.user.is_authenticated:
            return JsonResponse({'authenticate': False}, safe=False)
        return view_func(requests, *args, **kwargs)
    return wrapper


def user_login_json(request):
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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie_main')
                else:
                    messages.error(request, 'Invalid login')
                    return reverse('sign-in')
            else:
                messages.error(request, 'Вы не зарегистрированны')
                return redirect('sign-in')
    else:
        form = LoginForm()
    return render(request, 'base.html', {'form': form})


def user_logout(request):
    logout(request)
    return JsonResponse({'result': 'logout'})


@json_login_required
def index(request):
    return JsonResponse({'content': True}, safe=False)


def res_login(request):
    return render(request, 'res_login.html')
