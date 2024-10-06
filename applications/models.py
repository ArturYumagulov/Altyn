from django.contrib.auth import get_user_model
from django.db import models

from movies.models import Movie, Genre, Category, Kind, AgeLimit, MainShootingGroup
from regions.models import Speciality, Specialist, Region

User = get_user_model()

# Create your models here.


class Status(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=500, verbose_name="Статус")
    slug = models.SlugField()

    def __str__(self):
        return self.name


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
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    birthday = models.DateField(verbose_name="Дата рождения", blank=True, null=True, default=None)
    passport_number = models.CharField(verbose_name="Номер паспорта", blank=True, null=True, default=None,
                                       max_length=100)


# class ShootingGroupSpecialist(models.Model):
#     is_active = models.BooleanField(default=False, verbose_name="Активность")
#     name = models.CharField(max_length=1000, verbose_name="Наименование специальности")
#     slug = models.SlugField()
#
#     def __str__(self):
#         return f"{self.name}"
#
#     class Meta:
#         verbose_name_plural = "Специалист съемочной группы"
#         verbose_name = "Специалист съемочной группы"


# class MainShootingGroup(models.Model):
#
#     speciality = models.ForeignKey(ShootingGroupSpecialist, on_delete=models.PROTECT)
#     is_active = models.BooleanField(verbose_name="Активность", default=False)
#     last_name = models.CharField(max_length=150, verbose_name="Фамилия")
#     first_name = models.CharField(max_length=150, verbose_name="Имя")
#     birthday = models.DateField(
#         verbose_name="Дата рождения", blank=True, null=True, default=None
#     )
#     biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)
#
#     def __str__(self):
#         return f"{self.last_name} {self.first_name}"
#
#     class Meta:
#         verbose_name_plural = "Съемочная группа"
#         verbose_name = "Съемочные группы"


class MovieApp(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    name = models.CharField(max_length=500, verbose_name="Название фильма")
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Год выпуска")
    rolled_certificate = models.CharField(verbose_name="Прокатное удостоверение", null=True, blank=True, max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, verbose_name="Вид", blank=True, null=True, default=None)
    timing = models.CharField(verbose_name="Хронометраж", max_length=20)
    actors = models.TextField(verbose_name="В ролях",  blank=True, null=True, default=None)
    age_limit = models.ForeignKey(AgeLimit, on_delete=models.CASCADE, verbose_name="Возрастное ограничение")
    logline = models.TextField(verbose_name="Логлайн")
    debut = models.BooleanField(default=False, verbose_name="Дебютный")
    music = models.BooleanField(default=False, verbose_name="Оригинальная музыка")
    country = models.CharField(max_length=2000, verbose_name="Страна", blank=True, null=True, default=None)
    other_country = models.CharField(max_length=2000, verbose_name="Другая страна", blank=True, null=True, default=None)
    other_region = models.CharField(max_length=2000, verbose_name="Другой регион", blank=True, null=True, default=None)
    # movie = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name="Фильм")

    # Shooting_Group
    shooting_group = models.ManyToManyField(MainShootingGroup)
    other_shooting_group = models.TextField(verbose_name="Остальные члены съемочной команды", blank=True,
                                            null=True, default=None)

    agreement_to_placement = models.BooleanField(default=False, verbose_name="согласие на размещение на сайте",
                                                 null=True)
    agreement_to_vote = models.BooleanField(default=False, verbose_name="согласие на голосование", null=True)
    agreement_to_no_commerce_show = models.BooleanField(default=False, verbose_name="согласие на некоммерческие показы",
                                                        null=True)
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)

    portfolio = models.OneToOneField(MoviePortfolio, verbose_name="Ссылка на портфолио", on_delete=models.PROTECT)
    copyright_information = models.OneToOneField(CopyrightInformation, verbose_name="Информация о правообладателе",
                                                 on_delete=models.PROTECT)
    contract = models.OneToOneField(MovieContract, on_delete=models.PROTECT, verbose_name="Договор")

    genre = models.ManyToManyField(Genre, verbose_name="Жанр", blank=True, default=None)
    regions = models.ManyToManyField(Region, verbose_name="Регионы", blank=True, default=None)

    def __str__(self):
        return f"Заявка на фильм - {self.name}"


class SpecialistApp(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    other_speciality = models.CharField(verbose_name="Другая специальность", max_length=1000,
                                        blank=True, null=True, default=None)
    portfolio = models.URLField(verbose_name="Ссылка на портфолио", null=True, default=None)
    region = models.ManyToManyField(Region, verbose_name="Регион")
    city = models.CharField(verbose_name="Населенный пункт", max_length=1000, null=True, default=None)
    phone = models.CharField(verbose_name="Телефон", max_length=20, null=True, default=None)
    email = models.EmailField(max_length=225, verbose_name="Электронный адрес", null=True, default=None)
    social_link = models.TextField(verbose_name="Ссылка на социальные сети", null=True, default=None)
    descriptions = models.TextField(verbose_name="Дополнительно", null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус", null=True, default=None)
    biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)
    speciality = models.ManyToManyField(Speciality, related_name="app_specialities")

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

