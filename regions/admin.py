from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.Scenarist)
class ScenaristAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.Producer)
class ProducerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.Compositor)
class CompositorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.Operator)
class OperatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.ArtisticalDirector)
class ArtisticalDirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.CostumerDesigner)
class CostumerDesignerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('first_name', 'last_name')}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()


@admin.register(models.ScreeningPoint)
class ScreeningPointAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RegionalInternetResources)
class RegionalInternetResourcesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Production)
class ProductionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.RegionalProfile)
class RegionalProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.FilmmakersChat)
class FilmmakersChatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.LocationPhoto)
class LocationPhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RegionLocation)
class RegionLocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


@admin.register(models.Events)
class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
