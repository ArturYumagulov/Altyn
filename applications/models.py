from django.contrib.auth import get_user_model
from django.db import models

from movies.models import Movie, Genre, Category, Kind, AgeLimit, Region
from regions.models import Speciality, Specialist

User = get_user_model()

# Create your models here.


class Status(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=500, verbose_name="Статус")
    slug = models.SlugField()

    def __str__(self):
        return self.name


class AppDirector(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class AppScenarist(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class AppProducer(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class MoviePortfolio(models.Model):
    festivals = models.TextField(verbose_name="Участие в фестивалях")
    internet = models.TextField(verbose_name="Охват в интернете")
    smi = models.TextField(verbose_name="Публикации в СМИ")
    materials = models.TextField(verbose_name="Ссылка для скачивания материалов")


class CopyrightInformation(models.Model):
    possessor = models.TextField(verbose_name="Правообладатель")
    possessor_email = models.EmailField(verbose_name="Почта правообладателя")
    phone = models.CharField(verbose_name="Контакт для связи (телефон)", max_length=1000)
    contact_email = models.CharField(verbose_name="Контакт для связи (почта)", max_length=1000)


class MovieContract(models.Model):
    legal = models.BooleanField(verbose_name="Юридическое лицо", default=False)
    individual = models.BooleanField(verbose_name="Физическое лицо", default=False)
    organization_name = models.CharField(max_length=2000, verbose_name="Название организации", blank=True, null=True,
                                         default=None)
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    surname = models.CharField(verbose_name="Отчество", max_length=100, blank=True, null=True)
    movie_name = models.CharField(verbose_name="Отчество", max_length=100, blank=True, null=True)
    address = models.CharField(verbose_name="Адрес регистрации", max_length=1000, blank=True, null=True)
    inn = models.CharField(verbose_name="ИНН", max_length=1000, blank=True, null=True)
    payroll = models.CharField(verbose_name="Расчётный счёт", max_length=1000, blank=True, null=True)
    bank = models.CharField(verbose_name="Название банка", max_length=1000, blank=True, null=True)
    bik = models.CharField(verbose_name="БИК", max_length=1000, blank=True, null=True)
    correction = models.CharField(verbose_name="Коррекционный счет", max_length=1000, blank=True, null=True)


class MovieApp(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=500, verbose_name="Название фильма")
    # image = models.ImageField(upload_to="movie_image/", verbose_name="Картинка")
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Год выпуска")
    rolled_certificate = models.CharField(verbose_name="Прокатное удостоверение", null=True, blank=True,
                                          max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, verbose_name="Вид", blank=True, null=True, default=None)
    trailer = models.URLField()
    director = models.ForeignKey(
        AppDirector,
        on_delete=models.CASCADE,
        verbose_name="Режиссер",
        null=True,
        blank=True,
    )
    producer = models.ForeignKey(
        AppProducer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Продюссер",
    )
    scenarist = models.ForeignKey(
        AppScenarist,
        on_delete=models.CASCADE,
        verbose_name="Сценарист",
        null=True,
        blank=True,
    )

    # trailer = models.URLField()

    timing = models.CharField(verbose_name="Хронометраж", max_length=20)
    actors = models.TextField(verbose_name="В ролях")
    age_limit = models.ForeignKey(
        AgeLimit, on_delete=models.CASCADE, verbose_name="Возрастное ограничение"
    )
    logline = models.TextField(verbose_name="Логлайн")
    debut = models.BooleanField(default=False, verbose_name="Дебютный")
    music = models.BooleanField(default=False, verbose_name="Оригинальная музыка")
    country = models.CharField(max_length=2000, verbose_name="Страна", blank=True, null=True, default=None)
    other_region = models.CharField(max_length=2000, verbose_name="Другой регион", blank=True, null=True, default=None)
    slug = models.SlugField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name="Фильм")

    # Shooting_Group

    compositor_first_name = models.CharField(max_length=1000, verbose_name="Имя композитора", blank=True, null=True,
                                             default=None)
    compositor_last_name = models.CharField(max_length=1000, verbose_name="Фамилия композитора", blank=True, null=True,
                                            default=None)

    operator_first_name = models.CharField(max_length=1000)
    operator_last_name = models.CharField(max_length=1000)

    artistical_director_first_name = models.CharField(verbose_name="Имя художник постановщик", max_length=1000,
                                                      blank=True, null=True, default=None)
    artistical_director_last_name = models.CharField(verbose_name="Фамилия художник постановщик", max_length=1000,
                                                     blank=True, null=True, default=None)

    costume_designer_first_name = models.CharField(verbose_name="Имя художник по костюмам", max_length=1000, blank=True,
                                                   null=True, default=None)
    costume_designer_last_name = models.CharField(verbose_name="Имя художник по костюмам", max_length=1000, blank=True,
                                                  null=True, default=None)

    other_shooting_group = models.TextField(verbose_name="Остальные члены съемочной команды", blank=True,
                                            null=True, default=None)

    into_to_role = models.TextField(verbose_name="В ролях", blank=True, null=True, default=None)
    portfolio = models.OneToOneField(MoviePortfolio, verbose_name="Ссылка на портфолио", on_delete=models.PROTECT)
    copyright_information = models.OneToOneField(CopyrightInformation, verbose_name="Информация о правообладателе",
                                                 on_delete=models.PROTECT)
    agreement_to_placement = models.BooleanField(default=False, verbose_name="согласие на размещение на сайте")
    agreement_to_vote = models.BooleanField(default=False, verbose_name="согласие на голосование")
    agreement_to_no_commerce_show = models.BooleanField(default=False, verbose_name="согласие на некоммерческие показы")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)

    genre = models.ManyToManyField(Genre, verbose_name="Жанр", blank=True, default=None)



class SpecialistApp(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    speciality = models.ManyToManyField(Speciality, related_name="app_specialities")
    other_speciality = models.CharField(verbose_name="Другая специальность", max_length=1000,
                                        blank=True, null=True, default=None)
    portfolio = models.URLField(verbose_name="Ссылка на портфолио")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Регион")
    city = models.CharField(verbose_name="Населенный пункт", max_length=1000)
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    email = models.EmailField(max_length=225, verbose_name="Электронный адрес")
    social_link = models.TextField(verbose_name="Ссылка на социальные сети")
    descriptions = models.TextField(verbose_name="Дополнительно")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)
    spec = models.ForeignKey(Specialist, on_delete=models.PROTECT, blank=True, null=True, default=None)
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалист"


class InviteSpecialists(models.Model):

    email = models.EmailField(max_length=225, verbose_name="Электронный адрес")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    who_is = models.CharField(verbose_name="Кем является", max_length=1000, blank=True, null=True, default=None)
    accept = models.BooleanField(default=False, verbose_name="Принято")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self):
        return f"Приглашение для {self.email} от {self.user.email}"

    class Meta:
        ordering = ['created_date']

