from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats.base_formats import XLSX

from .models import Status, MovieApp, SpecialistApp, MoviePortfolio, MovieContract, CopyrightInformation
from .resources import MovieAppResource


# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MovieApp)
class MovieAppAdmin(ImportExportActionModelAdmin):
    resource_class = MovieAppResource
    formats = [XLSX]

    fields = (
        'user',
        'status',
        'name',
        'debut',
        'kind',
        'category',
        'genre',
        'timing',
        'logline',
        'year',
        'rolled_certificate',
        'age_limit',
        'country',
        'other_country',
        'regions',
        'other_region',
        'shooting_group',
        'other_shooting_group',
        'portfolio',
        'copyright_information',
        'contract'
    )


@admin.register(SpecialistApp)
class SpecialistAppAdmin(admin.ModelAdmin):
    pass


@admin.register(MoviePortfolio)
class MoviePortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(CopyrightInformation)
class CopyrightInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieContract)
class MovieContractAdmin(admin.ModelAdmin):
    pass
