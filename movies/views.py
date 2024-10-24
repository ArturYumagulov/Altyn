import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from movies.models import Almanac, Movie, Category, Genre, RatingStar, Rating, FavoriteMovie, Playlist
from regions.models import Region
from voting.models import Voting, Vote


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def movie_main(request):
    sliders = Almanac.objects.filter(on_slide=True).filter(is_active=True)
    almanacs = Almanac.objects.filter(is_active=True)

    context = {"sliders": sliders, "almanacs": almanacs}
    return render(request, "movies/main/main.html", context=context)


def movies(request):
    params = request.GET

    if len(params) == 0:
        queryset = Movie.objects.filter(is_active=True)
    else:
        almanac = params.getlist("almanac")
        category = params.getlist("category")
        genre = params.getlist("genre")
        region = params.getlist("regions")

        if almanac:
            queryset = Movie.objects.filter(
                Q(almanach__slug__in=almanac)
                | Q(regions__slug__in=region)
                | Q(category__slug__in=category)
                | Q(genre__slug__in=genre)
            ).filter(is_active=True).distinct()
        else:
            queryset = Movie.objects.filter(
                Q(regions__slug__in=region)
                | Q(category__slug__in=category)
                | Q(genre__slug__in=genre)
            ).filter(is_active=True).distinct()

    almanacs = (
        Almanac.objects.filter(laureate=False).values_list("pk", flat=True).distinct()
    )
    laureates = (
        Almanac.objects.filter(laureate=True).values_list("pk", flat=True).distinct()
    )

    filters = {
        "regions": Region.objects.filter(slug__in=queryset.values("regions__slug")).values("name", "slug"),
        "categories": {
            category["category__slug"]: category
            for category in queryset.values("category__name", "category__slug")
        }.values(),
        "genres": {
            genre["genre__slug"]: genre
            for genre in queryset.values("genre__name", "genre__slug")
        }.values(),
        "almanacs": queryset.filter(almanach__in=almanacs)
        .values("almanach__name", "almanach__slug")
        .distinct(),
        "laureates": queryset.filter(almanach__in=laureates)
        .values("almanach__name", "almanach__slug", "almanach__year")
        .distinct(),
    }
    context = {
        "filters": filters,
        "movies": queryset,
    }
    return render(request, "movies/movies/movies.html", context=context)


def get_json_filters(request):
    if request.method == "POST":
        params = request.GET
        data = json.loads(request.body)
        search = data.get("search")

        if len(params) == 0:
            queryset = Movie.objects.filter(is_active=True)
        else:
            almanac = params.getlist("almanac")
            category = params.getlist("category")
            genre = params.getlist("genre")
            region = params.getlist("regions")

            if almanac:
                queryset = Movie.objects.filter(
                    Q(almanach__slug__in=almanac)
                    | Q(regions__slug__in=region)
                    | Q(category__slug__in=category)
                    | Q(genre__slug__in=genre)
                ).distinct()
            else:
                queryset = Movie.objects.filter(
                    Q(regions__slug__in=region)
                    | Q(category__slug__in=category)
                    | Q(genre__slug__in=genre)
                ).distinct()

        almanacs = (
            Almanac.objects.filter(laureate=False)
            .values_list("pk", flat=True)
            .distinct()
        )
        laureates = (
            Almanac.objects.filter(laureate=True)
            .values_list("pk", flat=True)
            .distinct()
        )

        if data.get("type") == "regions":
            res = (
                Region.objects.filter(pk__in=queryset.values_list("regions", flat=True))
                .filter(name__icontains=search)
                .distinct()
            ).values("name", "slug")
            return JsonResponse({"result": list(res)}, safe=False)
        elif data.get("type") == "category":
            res = (
                Category.objects.filter(
                    pk__in=queryset.values_list("category", flat=True)
                )
                .filter(name__icontains=search)
                .distinct()
            ).values("name", "slug")
            return JsonResponse({"result": list(res)}, safe=False)
        elif data.get("type") == "genres":
            res = (
                Genre.objects.filter(pk__in=queryset.values_list("genre", flat=True))
                .filter(name__icontains=search)
                .distinct()
            ).values("name", "slug")
            return JsonResponse({"result": list(res)}, safe=False)
        elif data.get("type") == "laureates":
            res = (
                Almanac.objects.filter(
                    pk__in=queryset.filter(almanach__in=laureates)
                    .values_list("almanach", flat=True)
                    .distinct()
                )
                .filter(Q(name__icontains=search) | Q(year__icontains=search))
                .distinct()
            ).values("name", "slug", "year")

            return JsonResponse({"result": list(res)}, safe=False)

        elif data.get("type") == "almanacs":
            res = (
                Almanac.objects.filter(
                    pk__in=queryset.filter(almanach__in=almanacs)
                    .values_list("almanach", flat=True)
                    .distinct()
                )
                .filter(Q(name__icontains=search) | Q(year__icontains=search))
                .distinct()
            ).values("name", "slug", "year")

            return JsonResponse({"result": list(res)}, safe=False)

    return JsonResponse({"result": "method is not allowed"}, safe=False)


def movie_search(request):

    if request.method == "POST":
        search = str(json.loads(request.body).get("search")).lower().replace("ё", 'е')
        params = request.GET

        if len(params) == 0:
            queryset = Movie.objects.filter(search_name__icontains=search, is_active=True)

        else:
            almanac = params.getlist("almanac")
            category = params.getlist("category")
            genre = params.getlist("genre")
            region = params.getlist("regions")

            # Проверяем наличие фильтров и добавляем их по очереди

            queryset = Movie.objects.filter(is_active=True)

            # Проверяем наличие фильтров и добавляем их по очереди
            if almanac:
                queryset = queryset.filter(Q(almanach__slug__in=almanac))

            if region:
                queryset = queryset.filter(Q(regions__slug__in=region))

            if category:
                queryset = queryset.filter(Q(category__slug__in=category))

            if genre:
                queryset = queryset.filter(Q(genre__slug__in=genre))

            queryset = queryset.filter(search_name__icontains=search)

        result = {}

        for movie in queryset.values(
            "id",
            "name",
            "image",
            "rating",
            "year",
            "timing",
            "slug",
            "genre__name",
            "genre__slug",
        ):
            movie_id = movie["id"]
            genre = {"name": movie["genre__name"]}
            if movie_id not in result:
                result[movie_id] = {
                    "name": movie["name"],
                    "slug": movie["slug"],
                    "image": movie["image"],
                    "rating": queryset.get(pk=movie_id).get_avg_rating(),
                    "year": movie["year"],
                    "movie_time": movie["timing"],
                    "genres": [],
                }
            result[movie_id]["genres"].append(genre)

        json_result = list(result.values())

        return JsonResponse({"result": json_result}, safe=False)
    return JsonResponse({"result": "method is not allowed"}, safe=False)


def movie_detail(request, slug):
    movie = Movie.objects.prefetch_related("genre").get(slug=slug)
    ratings = RatingStar.objects.all()
    voting_status = Voting.objects.filter(movies=movie).exists()
    vote_status = request.user.pk in Vote.objects.filter(movie=movie).values_list("user", flat=True)
    voting_count = Vote.objects.filter(movie=movie).count()
    favorite = None

    if request.user.is_authenticated:
        favorite = movie.slug in FavoriteMovie.objects.filter(user=request.user).values_list("movie__slug", flat=True)

    context = {
        'movie': movie,
        'ratings': ratings,
        # 'rating_count': Rating.objects.filter(movie=movie).count(),
        'voting_status': voting_status,
        'vote_status': vote_status,
        'favorite': favorite,
        'voting_count': voting_count
    }

    return render(request, "movies/movies/movie_detail.html", context=context)


def get_star_rating(request):

    if request.method == "POST":
        ip = get_client_ip(request)
        movie_slug = json.loads(request.body).get('movieSlug')
        movie_star = json.loads(request.body).get('userRating')
        movie = get_object_or_404(Movie, slug=movie_slug)
        star = RatingStar.objects.get(value=movie_star)
        new_rating = Rating.objects.create(movie=movie, star=star, ip=ip)
        new_rating.save()
        return JsonResponse({'result': movie.get_avg_rating()})

    return render(request, 'movies/films_all.html')


def valid_user_ip(request):

    if request.method == "POST":
        movie = Movie.objects.get(slug=json.loads(request.body).get('slug'))
        ip = get_client_ip(request)
        movies_ips = Rating.objects.filter(movie=movie).values_list("ip", flat=True)
        if ip not in movies_ips:
            return JsonResponse({'valid': True}, safe=False)
        return JsonResponse({'valid': False}, safe=False)
    return JsonResponse({'valid': False}, safe=False)


def get_average_rating(request, slug):
    if request.method == "GET":
        movie = Movie.objects.get(slug=slug)
        return JsonResponse({'rating': movie.get_avg_rating()}, safe=False, status=200)


def add_to_favorites(request):
    if request.method == "POST":
        slug = json.loads(request.body).get('slug')
        movie = Movie.objects.get(slug=slug)
        favorite, created = FavoriteMovie.objects.get_or_create(user=request.user, movie=movie)

        if created:
            return JsonResponse({'result': True}, safe=True)

        return JsonResponse({'result': False}, safe=True)

    return JsonResponse({'result': False}, safe=True)


def remove_from_favorites(request):
    if request.method == "POST":
        slug = json.loads(request.body).get('slug')
        movie = Movie.objects.get(slug=slug)
        favorite = FavoriteMovie.objects.filter(user=request.user, movie=movie)

        if favorite.exists():
            favorite.delete()
            return JsonResponse({'result': True}, safe=True)
        else:
            return JsonResponse({'result': False}, safe=True)

    return JsonResponse({'result': False}, safe=True)


def playlists(request):
    if request.method == "POST":
        result = []
        slug = json.loads(request.body).get('slug')
        user_playlists = Playlist.objects.filter(user=request.user)
        data = {}

        for playlist in user_playlists:
            data['pk'] = playlist.pk
            data['name'] = playlist.name
            data['has_to_playlist'] = slug in playlist.movies.values_list('slug', flat=True)
            clen_data = data.copy()
            result.append(clen_data)
            data.clear()

        return JsonResponse({'result': True, 'playlists': result}, safe=True)
    return JsonResponse({'result': False}, safe=True)


def add_to_playlist(request):
    if request.method == "POST":
        data = json.loads(request.body)
        movie = Movie.objects.get(slug=data.get('slug'))
        playlist = Playlist.objects.get(pk=data.get('playlist_id'), user=request.user)
        if movie not in playlist.movies.all():
            playlist.movies.add(movie)
        return JsonResponse({'result': True}, safe=True)
    return JsonResponse({'result': 'Ошибка'}, safe=True)


def remove_from_playlist(request):
    if request.method == "POST":
        data = json.loads(request.body)
        movie = Movie.objects.get(slug=data.get('slug'))
        playlist = Playlist.objects.get(id=data.get('playlist_id'), user=request.user)
        if movie in playlist.movies.all():
            playlist.movies.remove(movie)
            playlist.save()
        return JsonResponse({'result': True}, safe=True)
    return JsonResponse({'result': False}, safe=True)


def add_playlist(request):
    if request.method == "POST":
        data = json.loads(request.body)
        movie = Movie.objects.get(slug=data.get('slug'))
        new_playlist = Playlist()
        new_playlist.user = request.user
        new_playlist.name = data.get('playlist_name')
        new_playlist.save()
        new_playlist.movies.add(movie)
        pk = new_playlist.pk
        return JsonResponse({'result': True, 'playlist_pk': pk}, safe=True)
    return JsonResponse({'result': False}, safe=True)
