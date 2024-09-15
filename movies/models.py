from datetime import datetime

from django.db import models
from django.db.models import Avg
from django.urls import reverse

# Create your models here.


def get_years():
    return {i: i for i in range(1970, datetime.now().year + 1)}


class Region(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Название", max_length=1000)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Регионы"
        verbose_name_plural = "Регион"

    def __str__(self):
        return self.name


class Genre(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Название", max_length=1000)
    group_1 = models.BooleanField(default=False, verbose_name="Группа 1")
    group_2 = models.BooleanField(default=False, verbose_name="Группа 2")
    slug = models.SlugField()

    class Meta:
        verbose_name = "Жанры"
        verbose_name_plural = "Жанр"

    def __str__(self):
        return self.name


class Kind(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Название", max_length=1000)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Типы"
        verbose_name_plural = "Тип"

    def __str__(self):
        return self.name


class Category(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Название", max_length=1000)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категория"

    def __str__(self):
        return self.name


class Status(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=500, verbose_name="Статус")
    show = models.BooleanField(verbose_name="Не показвать фильм", default=False)
    archive = models.BooleanField(verbose_name="Переносить в архив", default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Director(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Режиссер фильма"
        verbose_name_plural = "Режиссеры фильмов"


class Producer(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Продюссер"
        verbose_name_plural = "Продюссеры"


class Scenarist(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Сценарист"
        verbose_name_plural = "Сценаристы"


class Compositor(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Композитор"
        verbose_name_plural = "Композиторы"


class Operator(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"


class AgeLimit(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Возрастное ограничение", max_length=10)
    description = models.TextField(verbose_name="Описание", blank=True, null=True, default=None)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["pk"]
        verbose_name = "Возрастное ограничение"
        verbose_name_plural = "Возрастные ограничения"


class Almanach(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    main = models.BooleanField(verbose_name="Главный на странице", default=False)
    name = models.CharField(max_length=500, verbose_name="Альмонарх")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Альмонах"
        verbose_name_plural = "Альмонахи"


class RatingStar(models.Model):

    value = models.SmallIntegerField(verbose_name="Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        ordering = ["-value"]
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):

    ip = models.CharField(verbose_name="IP", max_length=15, unique=True)
    star = models.ForeignKey(
        RatingStar,
        on_delete=models.CASCADE,
        verbose_name="Оценка",
        related_name="ratings",
    )
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, verbose_name="Фильм")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.star}"

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class CategoryGenre(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=300, verbose_name="Название")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр вида"
        verbose_name_plural = "Жанр вида"


class RollerCertificate(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=300, verbose_name="Название")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Прокатное удостоверение"
        verbose_name_plural = "Прокатное удостоверение"


class Movie(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=500, verbose_name="Название фильма")
    image = models.ImageField(upload_to="movie_image/", verbose_name="Картинка")
    status = models.ForeignKey(
        Status, verbose_name="Статус", on_delete=models.CASCADE
    )
    region = models.ManyToManyField(Region, related_name="regions")
    year = models.DecimalField(
        max_digits=4, decimal_places=0, verbose_name="Год выпуска"
    )
    genre = models.ManyToManyField(Genre, verbose_name="Жанр", blank=True, default=None)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, verbose_name="Вид", blank=True, null=True, default=None)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        verbose_name="Режиссер",
        null=True,
        blank=True,
    )
    producer = models.ForeignKey(
        Producer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Продюссер",
    )
    scenarist = models.ForeignKey(
        Scenarist,
        on_delete=models.CASCADE,
        verbose_name="Сценарист",
        null=True,
        blank=True,
    )
    compositor = models.ForeignKey(
        Compositor,
        on_delete=models.CASCADE,
        verbose_name="Композитор",
        null=True,
        blank=True,
    )
    operator = models.ForeignKey(
        Operator,
        on_delete=models.CASCADE,
        verbose_name="Оператор",
        null=True,
        blank=True,
    )

    rolled_certificate = models.ForeignKey(RollerCertificate, on_delete=models.PROTECT,
                                           verbose_name="Прокатное удостоверение", null=True, blank=True
                                           )

    trailer = models.URLField()

    timing = models.CharField(verbose_name="Хронометраж", max_length=20)
    actors = models.TextField(verbose_name="В ролях")
    age_limit = models.ForeignKey(
        AgeLimit, on_delete=models.CASCADE, verbose_name="Возрастное ограничение"
    )
    descriptions = models.TextField(verbose_name="Описание")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    voting = models.TextField(
        verbose_name="Ссылка на голосование", blank=True, null=True, default=None
    )
    almanach = models.ManyToManyField(
        Almanach, verbose_name="Альманах", blank=True, default=None
    )
    close = models.BooleanField(default=False, verbose_name="Закрытый фильм")
    debut = models.BooleanField(default=False, verbose_name="Дебютный")
    music = models.BooleanField(default=False, verbose_name="Оригинальная музыка")
    country = models.CharField(max_length=2000, verbose_name="Страна", blank=True, null=True, default=None)
    other_region = models.CharField(max_length=2000, verbose_name="Другой регион", blank=True, null=True, default=None)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.slug})

    def get_avg_rating(self):
        movie = Movie.objects.get(pk=self.pk)
        stars = movie.rating_set.all()
        if len(stars) > 0:
            return (
                f"{round(stars.aggregate(Avg('star__value'))['star__value__avg'], 1)}"
            )
        else:
            return 0

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
