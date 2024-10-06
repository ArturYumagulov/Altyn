from django.contrib import admin
from django.utils.text import slugify

from movies import models


class MovieFilter(admin.SimpleListFilter):
    title = 'Фильмы'  # Заголовок фильтра
    parameter_name = 'movies'  # Параметр фильтра

    def lookups(self, request, model_admin):
        """
        Определяем, какие значения будут отображаться в фильтре.
        Возвращает список кортежей (value, verbose_name).
        """
        movies = models.Movie.objects.all()
        return [(movie.id, movie.name) for movie in movies]

    def queryset(self, request, queryset):
        """
        Фильтруем queryset в зависимости от выбранного значения фильтра.
        """
        if self.value():
            # Если значение выбрано, фильтруем участников по id фильма, связанного с ними
            return queryset.filter(movies__id=self.value())
        return queryset


# Register your models here.

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'status')


@admin.register(models.MovieStatus)
class ModelNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Kind)
class KindAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Almanac)
class AlmanacAdmin(admin.ModelAdmin):
    list_filter = ('laureate',)
    list_display = ('name', "year", 'is_active', 'laureate')
    prepopulated_fields = {"slug": ('name', 'year')}


@admin.register(models.AgeLimit)
class AgeLimitAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'description', 'pk', 'is_active')


@admin.register(models.RollerCertificate)
class RollerCertificateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.ShootingGroupSpecialist)
class ShootingGroupSpecialistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MainShootingGroup)
class MainShootingGroupAdmin(admin.ModelAdmin):
    list_display = ("speciality", 'get_movies')
    list_filter = (MovieFilter,)

    def get_movies(self, obj):
        """
        Метод для получения списка фильмов, в которых участвует данный член съемочной группы.
        """
        return ", ".join([movie.name for movie in obj.movies.all()])

    get_movies.short_description = "Фильм"  # Название столбца в админке
