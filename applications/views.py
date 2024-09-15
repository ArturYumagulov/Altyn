from django.http import HttpResponse
from django.shortcuts import render

from applications.services import send_word_via_email
from movies import models
from regions.models import Region, Speciality


# Create your views here.


def altyn_app(requests):

    kinds = models.Kind.objects.filter(is_active=True)
    categories = models.Category.objects.filter(is_active=True)
    genres_group_1 = models.Genre.objects.filter(group_1=True).filter(is_active=True)
    genres_group_2 = models.Genre.objects.filter(group_2=True).filter(is_active=True)
    rolled_certificates = models.RollerCertificate.objects.filter(is_active=True)
    age_limits = models.AgeLimit.objects.filter(is_active=True)
    regions = Region.objects.filter(other=False).filter(is_active=True)
    specialities = Speciality.objects.filter(is_active=True)

    context = {
        'kinds': kinds,
        'categories': categories,
        'genres_group_1': genres_group_1,
        'genres_group_2': genres_group_2,
        'rolled_certificates': rolled_certificates,
        'age_limits': age_limits,
        'regions': regions,
        'specialities': specialities,
    }
    return render(requests, 'applications/altyn_app/application.html', context=context)


def create_altyn_app(requests):
    if requests.method == "POST":
        print(requests.POST)
        return render(requests, "base.html")
    return render(requests, "base.html")


def send_docx(requests):
    send_word_via_email(requests)
    return HttpResponse("Ok")


