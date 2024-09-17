import json
from datetime import datetime

from regions.models import Region, Speciality
from .models import MovieApp, AppDirector, AppProducer, AppScenarist, MoviePortfolio, CopyrightInformation, Status, \
    InviteSpecialists, SpecialistApp, MovieContract
from movies.models import Category, Kind, RollerCertificate, AgeLimit, Genre
from .send_contract import send_word_via_email


def clean_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


def get_original_music(request):
    if request.get('music'):
        return {
            'compositor_first_name': request.get('compositor_first_name'),
            'compositor_last_name': request.get('compositor_last_name'),
        }
    return {
        'compositor_first_name': None,
        'compositor_last_name': None,
    }


def get_other_country(request):
    if request.get('other_country'):
        return {
            'other_country': request.get('other_country_name')
        }
    return {
            'other_country': request.get('other_country')
        }


def get_rolled_certificates(request):
    if request.get("rolled_certificate") == "est":
        return request.get("rolled_certificate_num")
    return RollerCertificate.objects.get(slug=request.get("rolled_certificate")).name


def legal_contract_context(new_contract):
    context = {
        'organization_name': new_contract.organization_name,
        'first_name': new_contract.first_name,
        'last_name': new_contract.last_name,
        'surname': new_contract.surname,
        'last_short': new_contract.last_name[0],
        'surname_short': new_contract.surname[0],
        'name': new_contract.movie_name,
        'address': new_contract.address,
        'inn': new_contract.inn,
        'payroll': new_contract.payroll,
        'bank': new_contract.bank,
        'bik': new_contract.bik,
        'correction': new_contract.correction,
        'created_date': f"{new_contract.created_date.year}-{new_contract.created_date.month}-"
                        f"{new_contract.created_date.day}"
    }
    return context


def individual_contract_context(new_contract):
    context = {
        'first_name': new_contract.first_name,
        'last_short': new_contract.last_name[0],
        'surname_short': new_contract.surname[0],
        'last_name': new_contract.last_name,
        'surname': new_contract.surname,
        'name': new_contract.movie_name,
        'passport_number': new_contract.passport_number,
        'birthday': new_contract.birthday
    }
    return context


def save_app(request):
    print(request)

    new_movie_app = MovieApp()

    new_movie_app.user = request.user
    new_movie_app.status = Status.objects.get(name="На рассмотрении")

    request = request.POST
    new_movie_app.name = request.get("name")
    new_movie_app.year = request.get("year")
    new_movie_app.rolled_certificate = get_rolled_certificates(request)
    new_movie_app.timing = request.get("timing")
    new_movie_app.actors = request.get("actors")
    new_movie_app.logline = request.get('logline')
    new_movie_app.debut = request.get('debut')
    new_movie_app.music = request.get('music')
    new_movie_app.country = request.get('country')
    new_movie_app.other_country = get_other_country(request)['other_country']

    new_movie_app.operator_first_name = request.get('operator_first_name')
    new_movie_app.operator_last_name = request.get('operator_last_name')

    new_movie_app.artistical_director_first_name = request.get('artistical_director_first_name')
    new_movie_app.artistical_director_last_name = request.get('artistical_director_last_name')

    new_movie_app.costume_designer_first_name = request.get('costume_designer_first_name')
    new_movie_app.costume_designer_last_name = request.get('costume_designer_last_name')

    new_movie_app.other_shooting_group = request.get('other_shooting_group')

    new_movie_app.agreement_to_placement = request.get('agreement_to_placement')
    new_movie_app.agreement_to_vote = request.get('agreement_to_vote')
    new_movie_app.agreement_to_no_commerce_show = request.get('agreement_to_no_commerce_show')

    # new_movie_app.save()

    # One2One

    portfolio = MoviePortfolio.objects.create(
        festivals=request.get('festivals'),
        internet=request.get('internet'),
        smi=request.get('smi'),
        materials=request.get('materials')
    )

    new_movie_app.portfolio = portfolio

    copyright_information = CopyrightInformation.objects.create(
        possessor=request.get('possessor'),
        possessor_email=request.get('possessor_email'),
        phone=request.get('phone'),
        contact_email=request.get('contact_email')
    )

    new_movie_app.copyright_information = copyright_information

    # ForeignKey
    new_movie_app.category = Category.objects.get(slug=request.get("category"))
    new_movie_app.kind = Kind.objects.get(slug=request.get("kind"))
    new_movie_app.age_limit = AgeLimit.objects.get(slug=request.get('age_limit'))

    # Режиссер
    new_director = AppDirector.objects.create(
        first_name=request.get("director_first_name"),
        last_name=request.get("director_last_name"),
        birthday=clean_date(request.get("director_birthday")),
        biography=request.get("director_biography"),
    )

    new_movie_app.director = new_director
    # Продюссер
    new_producer = AppProducer.objects.create(
        first_name=request.get("producer_first_name"),
        last_name=request.get("producer_last_name"),
        birthday=clean_date(request.get("producer_birthday")),
        biography=request.get("producer_biography"),
    )

    new_movie_app.producer = new_producer

    new_scenarist = AppScenarist.objects.create(
        first_name=request.get("scenarist_first_name"),
        last_name=request.get("scenarist_last_name"),
        birthday=clean_date(request.get("scenarist_birthday")),
        biography=request.get("scenarist_biography"),
    )

    new_movie_app.scenarist = new_scenarist

    #   Договор

    if request.get('contract_status') == 'now':

        new_contract = MovieContract()
        new_contract.organization_name = request.get('organization_name')
        new_contract.first_name = request.get('contract_first_name')
        new_contract.last_name = request.get('contract_last_name')
        new_contract.surname = request.get('contract_surname')
        new_contract.movie_name = request.get('movie_name')
        new_contract.address = request.get('address')
        new_contract.inn = request.get('inn')
        new_contract.payroll = request.get('payroll')
        new_contract.bank = request.get('bank')
        new_contract.bik = request.get('bik')
        new_contract.correction = request.get('correction')
        new_contract.save()

        if request.get('contract_type') == 'legal':
            send_word_via_email(
                "legal",
                context=legal_contract_context(new_contract),
                movie_name=new_contract.movie_name,
                email=new_movie_app.copyright_information.contact_email
            )
            new_contract.legal = True
            new_contract.save()
        elif request.get('contract_type') == 'individual':
            send_word_via_email(
                "individual",
                context=individual_contract_context(new_contract),
                movie_name=new_contract.movie_name,
                email=new_movie_app.copyright_information.contact_email
            )
            new_contract.individual = True
            new_contract.save()

        new_movie_app.contract = new_contract
    else:
        send_word_via_email("individual")

    #  Конец договор

    new_movie_app.save()

    # M2M
    for genre in request.getlist('genre'):
        new_movie_app.genre.add(Genre.objects.get(slug=genre))

    new_movie_app.save()

    for region in request.getlist('region'):
        new_movie_app.regions.add(Region.objects.get(slug=region))

    new_movie_app.save()


def save_invite(request):
    user = request.user
    request = request.POST

    for count in range(1, int(request.get('invite_count')) + 1):
        new_invite = InviteSpecialists()
        new_invite.user = user
        new_invite.email = request.get(f"invite_email_{count}")
        new_invite.first_name = request.get(f"invite_first_name_{count}")
        new_invite.last_name = request.get(f"invite_last_name_{count}")
        new_invite.who_is = request.get(f"invite_who_is_{count}")
        new_invite.save()
        #  Отправка письма


def create_region_speciality(request):

    new_region_specialist = SpecialistApp()
    new_region_specialist.user = request.user
    new_region_specialist.status = Status.objects.get(name="На рассмотрении")

    request = request.POST

    new_region_specialist.first_name = request.get('specialist_first_name')
    new_region_specialist.last_name = request.get('specialist_last_name')
    new_region_specialist.other_speciality = request.get('other_speciality')
    new_region_specialist.portfolio = request.get('speciality_portfolio_link')
    new_region_specialist.city = request.get('speciality_city')
    new_region_specialist.phone = request.get('speciality_phone')
    new_region_specialist.email = request.get('speciality_email')
    new_region_specialist.biography = request.get('speciality_biography')
    new_region_specialist.social_link = request.get('speciality_social_link')

    new_region_specialist.save()

    for region in request.getlist('speciality_region'):
        new_region_specialist.region.add(Region.objects.get(slug=region))

    new_region_specialist.save()

    for speciality in request.getlist('speciality'):
        new_region_specialist.speciality.add(Speciality.objects.get(slug=speciality))

    new_region_specialist.save()
