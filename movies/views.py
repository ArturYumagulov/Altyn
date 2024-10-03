import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from movies.models import Almanac, Movie, Category, Genre
from regions.models import Region


def movie_main(request):
    sliders = Almanac.objects.filter(on_slide=True).filter(is_active=True)
    almanacs = Almanac.objects.filter(is_active=True)

    context = {
        'sliders': sliders,
        'almanacs': almanacs
    }
    return render(request, "movies/main/main.html", context=context)


def all_movies(request):
    params = request.GET

    if len(params) == 0:
        queryset = Movie.objects.filter(is_active=True)
    else:
        almanac = params.getlist('almanac')
        category = params.getlist('category')
        genre = params.getlist('genre')
        region = params.getlist('regions')

        if almanac:
            queryset = Movie.objects.filter(
                Q(almanach__slug__in=almanac) |
                Q(regions__slug__in=region) |
                Q(category__slug__in=category) |
                Q(genre__slug__in=genre)
            ).distinct()
        else:
            queryset = Movie.objects.filter(
                Q(regions__slug__in=region) | Q(category__slug__in=category) | Q(genre__slug__in=genre)
            ).distinct()

    almanacs = Almanac.objects.filter(laureate=False).values_list('pk', flat=True).distinct()
    laureates = Almanac.objects.filter(laureate=True).values_list('pk', flat=True).distinct()

    filters = {
        'regions': queryset.values('regions__name', 'regions__slug').distinct(),
        'categories': queryset.values('category__name', 'category__slug').distinct(),
        'genres': queryset.values('genre__name', 'genre__slug', ).distinct(),
        'almanacs': queryset.filter(almanach__in=almanacs).values('almanach__name', 'almanach__slug').distinct(),
        'laureates': queryset.filter(almanach__in=laureates).values('almanach__name', 'almanach__slug', 'almanach__year').distinct()
    }
    context = {
        'filters': filters,
        'movies': queryset,
    }
    return render(request, 'movies/all_movies/all_movies.html', context=context)


def get_json_filters(request):
    if request.method == 'POST':
        params = request.GET
        data = json.loads(request.body)
        search = data.get('search')

        if len(params) == 0:
            queryset = Movie.objects.filter(is_active=True)
        else:
            almanac = params.get('almanac')
            category = params.getlist('category')
            genre = params.getlist('genre')
            region = params.getlist('regions')

            if almanac:
                queryset = Movie.objects.filter(
                    Q(almanach__slug__in=almanac) |
                    Q(regions__slug__in=region) |
                    Q(category__slug__in=category) |
                    Q(genre__slug__in=genre)
                ).distinct()
            else:
                queryset = Movie.objects.filter(
                    Q(regions__slug__in=region) | Q(category__slug__in=category) | Q(genre__slug__in=genre)
                ).distinct()

        almanacs = Almanac.objects.filter(laureate=False).values_list('pk', flat=True).distinct()
        laureates = Almanac.objects.filter(laureate=True).values_list('pk', flat=True).distinct()

        if data.get('type') == 'regions':
            res = (Region.objects.filter(pk__in=queryset.values_list("regions", flat=True))
                   .filter(name__icontains=search).distinct()).values('name', 'slug')
            return JsonResponse({'result': list(res)}, safe=False)
        elif data.get('type') == 'category':
            res = (Category.objects.filter(pk__in=queryset.values_list("category", flat=True))
                   .filter(name__icontains=search).distinct()).values("name", "slug")
            return JsonResponse({'result': list(res)}, safe=False)
        elif data.get('type') == 'genres':
            res = (Genre.objects.filter(pk__in=queryset.values_list("genre", flat=True))
                   .filter(name__icontains=search).distinct()).values("name", "slug")
            return JsonResponse({'result': list(res)}, safe=False)
        elif data.get('type') == 'laureates':
            res = (Almanac.objects.filter(pk__in=queryset.filter(almanach__in=laureates)
                                          .values_list("almanach", flat=True).distinct())
                   .filter(
                            Q(name__icontains=search) |
                            Q(year__icontains=search)
            ).distinct()).values("name", "slug", "year")

            return JsonResponse({'result': list(res)}, safe=False)

        elif data.get('type') == 'almanacs':
            res = (Almanac.objects.filter(pk__in=queryset.filter(almanach__in=almanacs)
                                          .values_list("almanach", flat=True).distinct())
                   .filter(
                            Q(name__icontains=search) |
                            Q(year__icontains=search)
            ).distinct()).values("name", "slug", "year")

            return JsonResponse({'result': list(res)}, safe=False)

    return JsonResponse({'result': "method is not allowed"}, safe=False)


def movie_search(request):
    if request.method == "POST":
        return JsonResponse({'result': True}, safe=False)
    return JsonResponse({'result': "method is not allowed"}, safe=False)
