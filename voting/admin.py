from django.contrib import admin

from voting.models import Vote, Voting


# Register your models here.


@admin.register(Vote)
class VotingAdmin(admin.ModelAdmin):
    pass


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Генерируем slug с использованием фамилии, имени и pk
        obj.slug = obj.slug + f'-{obj.pk}'
        # Снова сохраняем объект с обновленным slug
        obj.save()
