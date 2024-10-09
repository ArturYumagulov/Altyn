from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from movies import models
from movies.models import MainShootingGroup, Movie


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


class MainShootingGroupInline(admin.TabularInline):  # Можно также использовать admin.StackedInline
    model = models.Movie.shooting_group.through  # Используем промежуточную модель
    extra = 1  # Количество пустых строк для добавления новых записей
    verbose_name = 'Участник съемочной группы'  # В единственном числе
    verbose_name_plural = 'Участники съемочной группы'

    def get_queryset(self, request):
        # Ограничиваем список участников съемочной группы только для текущего фильма
        queryset = super().get_queryset(request)
        movie_id = request.resolver_match.kwargs.get('object_id')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)  # Фильтруем по текущему фильму
        return queryset


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    # inlines = [MainShootingGroupInline]
    # prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'status')
    fields = (
        'is_active',
        'close',
        'created_date',
        'status',
        'name',
        'user',
        'image',
        'year',
        'timing',
        'rolled_certificate',
        'get_debut',
        'country',
        'kind',
        'category',
        'other_region',
        'regions',
        'genre',
        'almanach',
        # ------------MainShootingGroup------------
        'director',
        'get_stage_director',
        'producer',
        'get_producer',
        'scenarist',
        'get_scenarist',
        'operator',
        'get_operator',
        'artistical_director',
        'get_artistical_director',
        'costumer_designer',
        'get_costumer_designer',
        'compositor',
        'get_compositor',
        'search_name',
        'slug',
        'edit_date',

    )
    readonly_fields = (
        'get_stage_director',
        'get_producer',
        'get_scenarist',
        'get_compositor',
        'get_operator',
        'get_artistical_director',
        'get_costumer_designer',
        'get_debut',
        'created_date',
        'edit_date'
    )

    def get_detail(self, spec_id):

        content = f"""
        <a target="_blank" style="margin-left: 20px;"class="related-widget-wrapper-link view-related" 
        id="view_id_Movie_shooting_group-0-mainshootinggroup" 
        data-href-template="/admin/movies/mainshootinggroup/__fk__/change/?_to_field=id" 
        title="Просмотреть выбранный объект" 
        href="/admin/movies/mainshootinggroup/{spec_id}/change/?_to_field=id">
        <img src="/static/admin/img/icon-viewlink.svg" alt="" width="20" height="20">
        </a>
        """
        return content

    def get_stage_director(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'stage-director':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} - {spec.birthday} {self.get_detail(spec.pk)}')
        context += '</ul>'
        return mark_safe(context)

    def get_producer(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'producer':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} - {spec.birthday} {self.get_detail(spec.pk)}</li>')
        context += '</ul>'
        return mark_safe(context)

    def get_scenarist(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'screenwriter':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} - {spec.birthday} {self.get_detail(spec.pk)}</li>')
        context += '</ul>'
        return mark_safe(context)

    def get_compositor(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'compositor':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} - {self.get_detail(spec.pk)}</li>')
            else:
                context = "-"
        context += '</ul>'
        return mark_safe(context)

    def get_operator(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'operator':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} {self.get_detail(spec.pk)}</li>')
        context += '</ul>'
        return mark_safe(context)

    def get_artistical_director(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'artistical_director':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} {self.get_detail(spec.pk)}</li>')
        context += '</ul>'
        return mark_safe(context)

    def get_costumer_designer(self, obj):
        context = '<ul class="list-group" style="margin-left: 0">'
        shooting_group = obj.shooting_group.all()
        for spec in shooting_group:
            if spec.speciality.slug == 'costumer_designer':
                context += (
                    f'<li class="list-group-item">{spec.last_name} '
                    f'{spec.first_name} {self.get_detail(spec.pk)}</li>')
        context += '</ul>'
        return mark_safe(context)

    def get_debut(self, obj):
        if obj.debut:
            return mark_safe("Да")
        return mark_safe("Нет")

    get_stage_director.short_description = 'Режиссеры в заявке'
    get_producer.short_description = 'Продюссеры в заявке'
    get_scenarist.short_description = 'Сценарист в заявке'
    get_compositor.short_description = 'Композитор в заявке'
    get_operator.short_description = 'Оператор в заявке'
    get_artistical_director.short_description = 'Художник постановщик в заявке'
    get_costumer_designer.short_description = 'Художник по костюмам'
    get_debut.short_description = 'Дебют'


    class Media:
        js = (
            'js/admin.js',  # Путь к вашему JS файлу внутри static
        )


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


@admin.register(models.FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    pass
