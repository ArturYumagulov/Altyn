from django.contrib import admin

from movies import models


# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Status)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Kind)
class KindAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Almanach)
class AlmanachAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AgeLimit)
class AgeLimitAdmin(admin.ModelAdmin):
    pass
