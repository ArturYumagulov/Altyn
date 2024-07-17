import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.forms import LoginForm


# from django.contrib.auth.decorators import login_required


# Create your views here.

def res_user_login(request):
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
                    # messages.error(request, 'Invalid login')
                    return reverse('sign-in')
            else:
                # messages.error(request, 'Вы не зарегистрированны')
                return HttpResponse
    else:
        form = LoginForm()
    return render(request, 'base.html', {'form': form})


def res_login_page(request):
    return render(request, 'res_login.html')
