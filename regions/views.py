from django.shortcuts import render

from regions.models import Region, ScreeningPoint, RegionalInternetResources


# Create your views here.


def main(requests):

    regions = Region.objects.filter(is_active=True)

    context = {
        'regions': regions,
    }

    if len(requests.GET) > 0:
        region = Region.objects.get(slug=requests.GET.get('region'))
        screening_points = ScreeningPoint.objects.filter(is_active=True, region=region)
        internet_resources = RegionalInternetResources.objects.filter(is_active=True, region=region)

        context['screening_points'] = screening_points[:2]
        context['internet_resources'] = internet_resources[:2]

    return render(requests, 'regions/main.html', context=context)
