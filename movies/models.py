from datetime import datetime

from django.db import models
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
        ordering = ['pk']
        verbose_name = "Статус фильма"
        verbose_name_plural = "Статусы фильмов"


class Director(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ['last_name']
        verbose_name = "Режиссер фильма"
        verbose_name_plural = "Режиссеры фильмов"


class Producer(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ['last_name']
        verbose_name = "Продюссер"
        verbose_name_plural = "Продюссеры"


class Scenarist(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ['last_name']
        verbose_name = "Сценарист"
        verbose_name_plural = "Сценаристы"


class Movie(models.Model):

    name = models.CharField(max_length=500, verbose_name="Название фильма")
    image = models.ImageField(upload_to="movie_image/", verbose_name="Картинка")
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Год выпуска")
    genre = models.ManyToManyField(Genre, verbose_name="Жанр", blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="Режиссер")
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Продюссер")
    scenarist = models.ForeignKey()

    descriptions = models.TextField(verbose_name="Описание")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    voting = models.TextField(verbose_name='Ссылка на голосование', blank=True, null=True, default=None)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={'slug': self.slug})

    def get_avg_rating(self):
        movie = Movie.objects.get(pk=self.pk)
        stars = movie.rating_set.all()
        if len(stars) > 0:
            return f"{round(stars.aggregate(Avg('star__value'))['star__value__avg'], 1)}"
        else:
            return 0

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_date']
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"



