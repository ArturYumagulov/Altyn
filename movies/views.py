from django.shortcuts import render

from movies.models import Almanac


def movie_main(request):
    sliders = Almanac.objects.filter(on_slide=True).filter(is_active=True)
    almanacs = Almanac.objects.filter(is_active=True).exclude(on_slide=True)

    context = {
        'sliders': sliders,
        'almanacs': almanacs
    }
    return render(request, "movies/main/main.html", context=context)
