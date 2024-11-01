import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from regions.models import (Region, ScreeningPoint, RegionalInternetResources, Production, Specialist,
                            RegionalProfile, FilmmakersChat, RegionLocation, Events, Speciality)


# Create your views here.


def main(requests):

    regions = Region.objects.filter(
        Q(screeningpoint__isnull=False) |
        Q(regionalinternetresources__isnull=False) |
        Q(production__isnull=False) |
        Q(regionalprofile__isnull=False) |
        Q(filmmakerschat__isnull=False) |
        Q(specialist__isnull=False) |
        Q(events__isnull=False)
    ).distinct()

    context = {
        'regions': regions,
    }

    region = Region.objects.get(name="Республика Татарстан")
    screening_points = ScreeningPoint.objects.filter(is_active=True, region=region)[:2]
    internet_resources = RegionalInternetResources.objects.filter(is_active=True, region=region)[:2]
    productions = Production.objects.filter(is_active=True, region=region)[:2]
    specialists = Specialist.objects.filter(is_active=True, region=region)[:2]
    regional_profile = RegionalProfile.objects.filter(is_active=True, region=region).last()
    chats = FilmmakersChat.objects.filter(is_active=True, region=region)[:2]
    locations = RegionLocation.objects.filter(is_active=True, region=region)[:2]
    event = Events.objects.filter(is_active=True, region=region).last()

    context['screening_points'] = screening_points
    context['internet_resources'] = internet_resources
    context['productions'] = productions
    context['specialists'] = specialists
    context['regional_profile'] = regional_profile
    context['chats'] = chats
    context['locations'] = locations
    context['event'] = event

    return render(requests, 'regions/main.html', context=context)


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
