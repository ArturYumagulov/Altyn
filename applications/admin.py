from django.contrib import admin
from .models import Status, AppDirector, AppProducer, AppScenarist, MovieApp, SpecialistApp

# Register your models here.


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(AppDirector)
class AppDirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieApp)
class MovieAppAdmin(admin.ModelAdmin):
    pass


@admin.register(SpecialistApp)
class SpecialistAppAdmin(admin.ModelAdmin):
    pass



