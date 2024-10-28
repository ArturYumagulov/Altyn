from django.shortcuts import render

from regions.models import Region, ScreeningPoint, RegionalInternetResources, Production


# Create your views here.


def main(requests):

    regions = Region.objects.filter(is_active=True)

    context = {
        'regions': regions,
    }

    if len(requests.GET) > 0:
        region = Region.objects.get(slug=requests.GET.get('region'))
        screening_points = ScreeningPoint.objects.filter(is_active=True, region=region)[:2]
        internet_resources = RegionalInternetResources.objects.filter(is_active=True, region=region)[:2]
        productions = Production.objects.filter(is_active=True, region=region)[:2]

        context['screening_points'] = screening_points
        context['internet_resources'] = internet_resources
        context['productions'] = productions

    return render(requests, 'regions/main.html', context=context)
