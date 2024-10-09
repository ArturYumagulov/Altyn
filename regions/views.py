from django.shortcuts import render

from regions.models import Region


# Create your views here.


def main(requests):
    regions = Region.objects.filter(is_active=True)

    context = {
        'regions': regions,
    }
    return render(requests, 'regions/main.html', context=context)
