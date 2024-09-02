from django.contrib import admin

from voting.models import Voting, VoteItem


# Register your models here.


@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    pass


@admin.register(VoteItem)
class VoteItemAdmin(admin.ModelAdmin):
    pass

