import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.forms import LoginForm
User = get_user_model()

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


def verify_email(request, token):
    try:
        user = User.objects.get(verify_token=token)
        user.is_active = True
        user.save()
        return render(request, 'users/register/verify_email_done.html')
    except User.DoesNotExist:
        return HttpResponse('<h1>Error</h1>')


def change_password(request):
    return render(request, 'users/register/change-password.html')


def reset_pass_form(request, token):
    try:
        User.objects.get(verify_token=token)
        return render(request, 'users/register/password-reset.html')

    except User.DoesNotExist:
        return JsonResponse({'result': False}, safe=False)


@login_required
def profile(request):

    user = User.objects.get(pk=request.user.pk)

    context = {
        'user': user
    }

    return render(request, 'users/profile/profile.html', context=context)


@login_required
def edit_profile(request):
    return render(request, 'users/profile/edit_profile.html')
