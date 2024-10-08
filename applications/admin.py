from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats.base_formats import XLSX

from .models import Status, MovieApp, SpecialistApp
from .resources import MovieAppResource


# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MovieApp)
class MovieAppAdmin(ImportExportActionModelAdmin):
    resource_class = MovieAppResource
    formats = [XLSX]


@admin.register(SpecialistApp)
class SpecialistAppAdmin(admin.ModelAdmin):
    pass
