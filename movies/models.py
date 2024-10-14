from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from django.urls import reverse

from regions.models import Region, Director, Producer, Scenarist, Compositor, Operator, ArtisticalDirector, \
    CostumerDesigner

# Create your models here.

User = get_user_model()


def get_years():
    return {i: i for i in range(1970, datetime.now().year + 1)}


class ShootingGroupSpecialist(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(max_length=1000, verbose_name="Наименование специальности")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Специалист съемочной группы"
        verbose_name = "Специалист съемочной группы"


class MainShootingGroup(models.Model):

    speciality = models.ForeignKey(ShootingGroupSpecialist, on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.speciality.name} - {self.last_name} {self.first_name}"

    class Meta:
        verbose_name_plural = "Съемочная группа"
        verbose_name = "Съемочные группы"


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


class MovieStatus(models.Model):

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


class AgeLimit(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Возрастное ограничение", max_length=10)
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True, default=None
    )
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["pk"]
        verbose_name = "Возрастное ограничение"
        verbose_name_plural = "Возрастные ограничения"


class Almanac(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    on_slide = models.BooleanField(verbose_name="На слайде", default=False)
    slide_image = models.ImageField(upload_to="movies/main/slides", verbose_name="Картинка слайдера", default=None,
                                    null=True, blank=True)
    name = models.CharField(max_length=500, verbose_name="Название")
    short_name = models.CharField(max_length=30, verbose_name="Короткое название", blank=True, null=True, default=None)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="movies/main/slides", verbose_name="Картинка")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    laureate = models.BooleanField(default=False, verbose_name="Лауреат")
    year = models.CharField(
        verbose_name="Год",
        default=None,
        blank=True,
        null=True,
        max_length=4
    )
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name} - {self.year}"

    def get_absolute_url(self):
        return reverse("almanarch_detail", kwargs={'slug': self.slug})

    class Meta:
        ordering = ["name"]
        verbose_name = "Альманах"
        verbose_name_plural = "Альманахи"


class RatingStar(models.Model):

    value = models.SmallIntegerField(verbose_name="Значение", default=0)

    def __str__(self):
        return f"{self.value}"

    class Meta:
        ordering = ["value"]
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):

    ip = models.CharField(verbose_name="IP", max_length=15)
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
    """Фильм"""

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Добавил")
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(max_length=500, verbose_name="Название фильма")
    search_name = models.CharField(max_length=500, verbose_name="Название для поиска", blank=True)
    image = models.ImageField(upload_to="movie_image/", verbose_name="Картинка")
    status = models.ForeignKey(MovieStatus, verbose_name="Статус", on_delete=models.CASCADE)
    regions = models.ManyToManyField(Region, related_name="movie_regions")
    year = models.DecimalField(max_digits=4, decimal_places=0, verbose_name="Год выпуска")
    genre = models.ManyToManyField(Genre, verbose_name="Жанр", blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    almanach = models.ManyToManyField(Almanac, verbose_name="Альманах", blank=True, default=None)
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT, verbose_name="Вид", blank=True, null=True, default=None)
    rolled_certificate = models.CharField(verbose_name="Прокатное удостоверение", null=True, blank=True,
                                          max_length=1000)
    timing = models.CharField(verbose_name="Хронометраж", max_length=20)
    actors = models.TextField(verbose_name="В ролях")
    age_limit = models.ForeignKey(AgeLimit, on_delete=models.CASCADE, verbose_name="Возрастное ограничение")
    descriptions = models.TextField(verbose_name="Описание")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    vk_iframe = models.TextField(verbose_name="Ссылка на iframe - фильм", blank=True, null=True, default=None)
    close = models.BooleanField(default=False, verbose_name="Закрытый фильм")
    debut = models.BooleanField(default=False, verbose_name="Дебютный")
    music = models.BooleanField(default=False, verbose_name="Оригинальная музыка")
    country = models.CharField(max_length=2000, verbose_name="Страна", blank=True, null=True, default=None)
    other_region = models.CharField(max_length=2000, verbose_name="Другой регион", blank=True, null=True, default=None)
    director = models.ManyToManyField(Director, verbose_name="Режиссеры-регион", blank=True, related_name='directors')
    producer = models.ManyToManyField(Producer, blank=True, verbose_name="Продюссеры-регион", related_name="producers")
    scenarist = models.ManyToManyField(Scenarist, verbose_name="Сценарист-регион", blank=True,
                                       related_name="scenarists")
    compositor = models.ManyToManyField(Compositor, verbose_name="Композитор-регион", blank=True)
    operator = models.ManyToManyField(Operator, verbose_name="Оператор-регион", blank=True)
    artistical_director = models.ManyToManyField(ArtisticalDirector, verbose_name="Художник постановщик", blank=True)
    costumer_designer = models.ManyToManyField(CostumerDesigner, verbose_name="Художник по костюмам", blank=True)
    shooting_group = models.ManyToManyField(MainShootingGroup, verbose_name="Съемочная группа", blank=True,
                                            related_name='movies')
    trailer = models.TextField(verbose_name="Ссылка на iframe - трейлер", blank=True, null=True, default=None)
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

    # def get_voting_count(self):
    #     voting_count = Vote.objects.filter(movie=self).count(),
    #     return voting_count[0]

    def save(self, *args, **kwargs):
        self.search_name = self.name.lower().replace("ё", 'е')  # Приведение к нижнему регистру перед сохранением
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["created_date"]
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name='favorite_movies')
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE, related_name='favorites')
    added_date = models.DateField(verbose_name="Дата добавления", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.name}"

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-added_date']
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"


class Playlist(models.Model):
    """Модель плейлиста"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists",
                             verbose_name="Пользователь")
    name = models.CharField(max_length=255, verbose_name="Название плейлиста")
    description = models.TextField(blank=True, null=True, verbose_name="Описание плейлиста")
    movies = models.ManyToManyField(Movie, related_name="playlists", verbose_name="Фильмы в плейлисте", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def get_last_movie_image(self):
        # Получаем последний добавленный фильм, сортируя по дате добавления
        last_movie = self.movies.order_by('-id').first()

        # Проверяем, если фильм существует и у него есть картинка
        if last_movie and last_movie.image:
            return last_movie.image.url
        return None  # Если фильм или картинка отсутствуют

    class Meta:
        verbose_name = "Плейлист"
        verbose_name_plural = "Плейлисты"
        ordering = ["-created_at"]
