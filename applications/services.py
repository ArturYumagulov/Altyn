from datetime import datetime

from django.contrib.auth import get_user_model

from movies.models import Category, Kind, RollerCertificate, Movie, AgeLimit
from .models import MovieApp, Status, AppDirector, AppProducer, AppScenarist

user = get_user_model()


def clean_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


def get_rolled_certificates(request):
    if request.get("rolled_certificate") == "est":
        return request.get("rolled_certificate_num")
    return RollerCertificate.objects.get(slug=request.get("rolled_certificate")).name


def save_app(request):
    print(request)

    new_movie_app = MovieApp()

    new_movie_app.user = user.objects.get(request.user.pk)
    new_movie_app.status = Status.objects.get(name="на рассмотрении")

    request = request.POST
    new_movie_app.name = request.get("name")
    new_movie_app.year = request.get("year")
    new_movie_app.rolled_certificate = get_rolled_certificates(request)
    new_movie_app.timing = request.get("timing")
    new_movie_app.actors = request.get("actors")
    new_movie_app.logline = request.get('logline')

    # ForeignKey
    new_movie_app.category = Category.objects.get(slug=request.get("category"))
    new_movie_app.kind = Kind.objects.get(slug=request.get("kind"))
    new_movie_app.age_limit = AgeLimit.objects.get(slug=request.get('age_limit'))

    # Режиссер
    new_director = AppDirector.objects.update_or_create(
        first_name=request.get("director_first_name"),
        last_name=request.get("director_last_name"),
        birthday=clean_date(request.get("director_birthday")),
        biography=request.get("director_biography"),
    )

    new_movie_app.director = new_director
    # Продюссер
    new_producer = AppProducer.objects.update_or_create(
        first_name=request.get("producer_first_name"),
        last_name=request.get("producer_last_name"),
        birthday=clean_date(request.get("producer_birthday")),
        biography=request.get("producer_biography"),
    )

    new_movie_app.producer = new_producer

    new_scenarist = AppScenarist.objects.update_or_create(
        first_name=request.get("scenarist_first_name"),
        last_name=request.get("scenarist_last_name"),
        birthday=clean_date(request.get("scenarist_birthday")),
        biography=request.get("scenarist_biography"),
    )

    new_movie_app.scenarist = new_scenarist
