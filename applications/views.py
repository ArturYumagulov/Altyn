from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from applications.services import save_app, create_region_speciality, save_invite, save_movie
from movies import models
from regions.models import Region, Speciality


# Create your views here.

@login_required
def altyn_app_page(requests):

    kinds = models.Kind.objects.filter(is_active=True)
    categories = models.Category.objects.filter(is_active=True)
    genres_group_1 = models.Genre.objects.filter(group_1=True).filter(is_active=True)
    genres_group_2 = models.Genre.objects.filter(group_2=True).filter(is_active=True)
    rolled_certificates = models.RollerCertificate.objects.filter(is_active=True)
    age_limits = models.AgeLimit.objects.filter(is_active=True)
    regions = Region.objects.filter(other=False).filter(is_active=True)
    specialities = Speciality.objects.filter(is_active=True)

    context = {
        "kinds": kinds,
        "categories": categories,
        "genres_group_1": list(genres_group_1.values("name", "slug", "pk")),
        "genres_group_2": list(genres_group_2.values("name", "slug", "pk")),
        "rolled_certificates": rolled_certificates,
        "age_limits": age_limits,
        "regions": regions,
        "specialities": specialities,
    }
    return render(requests, "applications/altyn_app/application.html", context=context)


def create_altyn_app(request):
    if request.method == "POST":

        if request.user.is_authenticated:
            invite_count = int(request.POST.get('invite_count'))  # Количество приглашений
            if request.POST.get('region_map'):
                create_region_speciality(request)
            if invite_count > 0:
                save_invite(request)
            save_movie(request)
            save_app(request)
            return HttpResponse(
                '<h1>OK</h1>'
            )
        else:
            return render(request, "res_login.html")
    return render(request, "base.html")


def send_docx(requests):
    # send_word_via_email(requests)
    return HttpResponse("Ok")
