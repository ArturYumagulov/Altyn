from django.contrib import admin

from movies import models


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
