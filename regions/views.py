import json

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db.models import Q

from regions.models import (Region, ScreeningPoint, RegionalInternetResources, Production, Specialist,
                            RegionalProfile, FilmmakersChat, RegionLocation, Events, Speciality, Location)


# Create your views here.

@cache_page(60*15)
def main(request):
    try:
        if len(request.GET) > 0:
            region_slug = request.GET.get('region')

            regions = Region.objects.filter(
                Q(screeningpoint__isnull=False) |
                Q(regionalinternetresources__isnull=False) |
                Q(production__isnull=False) |
                Q(regionalprofile__isnull=False) |
                Q(filmmakerschat__isnull=False) |
                Q(specialist__isnull=False) |
                Q(events__isnull=False) |
                Q(regionlocation__isnull=False)
            ).distinct()

            region = Region.objects.get(slug=region_slug)
            screening_points = ScreeningPoint.objects.filter(is_active=True, region=region)[:2]
            internet_resources = RegionalInternetResources.objects.filter(is_active=True, region=region)[:2]
            productions = Production.objects.filter(is_active=True, region=region)[:2]
            specialists = Specialist.objects.filter(is_active=True, region=region)[:2]
            regional_profile = RegionalProfile.objects.filter(is_active=True, region=region).last()
            chats = FilmmakersChat.objects.filter(is_active=True, region=region)[:2]
            locations = RegionLocation.objects.filter(is_active=True, region=region)[:2]
            event = Events.objects.filter(is_active=True, region=region).last()
            context = {
                'regions': regions,
                'screening_points': screening_points,
                'internet_resources': internet_resources,
                'productions': productions,
                'specialists': specialists,
                'regional_profile': regional_profile,
                'chats': chats,
                'locations': locations,
                'event': event,
                'region_slug': region_slug,
            }
            return render(request, 'regions/main_utils/main.html', context=context)
    except Region.DoesNotExist:
        return render(request, 'base.html')


def get_region_resources(request):
    if request.method == "POST":
        try:
            slug = json.loads(request.body).get('slug')
            region = Region.objects.get(slug=slug)

            screening_points = ScreeningPoint.objects.filter(is_active=True, region=region)[:2]
            internet_resources = RegionalInternetResources.objects.filter(is_active=True, region=region)[:2]
            productions = Production.objects.filter(is_active=True, region=region)[:2]
            specialists = Specialist.objects.filter(is_active=True, region=region).prefetch_related('speciality')[:2]
            regional_profile = RegionalProfile.objects.filter(is_active=True, region=region)[:1]
            chats = FilmmakersChat.objects.filter(is_active=True, region=region)[:2]
            locations = RegionLocation.objects.filter(is_active=True, region=region)[:2]
            event = Events.objects.filter(is_active=True, region=region)[:1]

            # Формируем результат с раскрытием связей M2M
            result = {
                'screening_points': list(screening_points.values(
                    'image', 'name', 'address', 'phone', 'social_net', 'site', 'email'
                )),
                'internet_resources': list(internet_resources.values(
                    'name', 'region__name', 'link'
                )),
                'productions': list(productions.values(
                    'logo', 'name', 'services_type', 'phone', 'social_net', 'site', 'email'
                )),
                'specialists': [
                    {
                        'first_name': specialist.first_name,
                        'last_name': specialist.last_name,
                        'photo': specialist.photo.url if specialist.photo else None,
                        'speciality': list(specialist.speciality.values('name')),
                        'phone': specialist.phone,
                        'email': specialist.email
                    }
                    for specialist in specialists
                ],
                'regional_profile': list(regional_profile.values(
                    'photo', 'name', 'citation', 'author', 'author_city__name', 'slug'
                )),
                'chats': list(chats.values('name', 'region__name', 'link_to_chat')),
                'locations': list(locations.values('main_photo', 'name', 'slug')),
                'event': list(event.values('photo', 'name', 'descriptions', 'slug'))
            }

            return JsonResponse({'detail': True, 'result': result})

        except ObjectDoesNotExist:
            return JsonResponse({'detail': False, 'error': 'Region not found'}, status=404)

    return JsonResponse({'detail': False, 'error': 'Invalid request method'}, status=400)


def screenpoint_detail(request, slug):
    """Точки кинопоказов"""

    screening_points = ScreeningPoint.objects.filter(is_active=True, region__slug=slug)

    paginator = Paginator(screening_points, 10)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    return render(request, 'regions/details/screening_points.html',
                  context={'screening_points': pages, 'slug': slug, 'paginator': paginator})


def internet_resources_detail(request, slug):
    """Интернет ресурсы"""

    internet_resources = RegionalInternetResources.objects.filter(is_active=True, region__slug=slug)

    paginator = Paginator(internet_resources, 10)
    page_number = request.GET.get('page')
    pages = paginator.get_page(page_number)

    return render(request, 'regions/details/internet-resources.html',
                  context={
                            'internet_resources': pages, 'slug': slug, 'paginator': paginator})


def get_resource_context(request, queryset, slug):
    context = {}
    paginator = Paginator(queryset, 8)
    page_number = request.GET.get('page')

    context['contents'] = paginator.get_page(page_number)
    context['paginator'] = paginator
    context['region_slug'] = slug

    return context


def resources_detail(request, resource_type, slug):

    if resource_type == 'screening-points':
        screening_points = ScreeningPoint.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, screening_points, slug)
        return render(request, 'regions/details/screening_points.html', context=context)

    elif resource_type == 'internet-resources':
        internet_resources = RegionalInternetResources.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, internet_resources, slug)
        return render(request, 'regions/details/internet-resources.html', context=context)

    elif resource_type == 'productions':
        productions = Production.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, productions, slug)
        return render(request, 'regions/details/productions.html', context=context)

    elif resource_type == 'specialists':

        specialists = Specialist.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, specialists, slug)
        return render(request, 'regions/details/specialists.html', context=context)

    elif resource_type == 'portrait':

        portraits = RegionalProfile.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, portraits, slug)
        return render(request, 'regions/details/portraits.html', context=context)

    elif resource_type == 'chats':
        chats = FilmmakersChat.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, chats, slug)
        return render(request, 'regions/details/chats.html', context=context)

    elif resource_type == 'locations':
        locations = RegionLocation.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, locations, slug)
        return render(request, 'regions/details/locations.html', context=context)

    elif resource_type == 'events':
        events = Events.objects.filter(is_active=True, region__slug=slug)
        context = get_resource_context(request, events, slug)
        return render(request, 'regions/details/events.html', context=context)

    return HttpResponse(f"{resource_type} - {slug}")


def portrait_detail(request, pk):
    try:
        portrait = RegionalProfile.objects.get(pk=pk)
        return render(request, 'regions/details/portrait_detail.html', context={'portrait': portrait})
    except RegionalProfile.DoesNotExist:
        return HttpResponse('Error')


def location_detail(request, pk):
    try:
        location = RegionLocation.objects.get(pk=pk)
        return render(request, 'regions/details/location_detail.html', context={'location': location})
    except RegionalProfile.DoesNotExist:
        return HttpResponse('Error')
