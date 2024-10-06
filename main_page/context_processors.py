from django.utils import timezone

from voting.models import Voting


def voting_context(request):
    now = timezone.now()
    active_voting = Voting.objects.filter(start_date__lte=now, end_date__gte=now)
    return {'active_voting': active_voting.first()}
