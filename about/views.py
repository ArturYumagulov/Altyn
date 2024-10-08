from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def about(request):
    return render(request, 'about/about.html')
