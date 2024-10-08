from import_export import resources

from .models import Vote


class VoteResource(resources.ModelResource):
    class Meta:
        model = Vote
        fields = ('user__email', 'movie__name')

