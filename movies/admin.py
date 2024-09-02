from django.contrib import admin

from movies import models


# Register your models here.

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Status)
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


@admin.register(models.Almanach)
class AlmanachAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.AgeLimit)
class AgeLimitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
