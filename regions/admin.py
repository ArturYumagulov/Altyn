from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    pass
