from django.contrib import admin

from voting.models import Vote, Voting


# Register your models here.


@admin.register(Vote)
class VotingAdmin(admin.ModelAdmin):
    pass


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    pass
