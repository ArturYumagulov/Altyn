from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export.formats.base_formats import XLSX

from .models import Vote, Voting
from .resources import VoteResource


# Register your models here.


@admin.register(Vote)
class VoteAdmin(ImportExportActionModelAdmin):
    resource_class = VoteResource
    formats = [XLSX]


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     # Генерируем slug с использованием фамилии, имени и pk
    #     obj.slug = obj.slug + f'-{obj.pk}'
    #     # Снова сохраняем объект с обновленным slug
    #     obj.save()
