import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from movies.models import Movie
from voting.models import Vote

# Create your views here

User = get_user_model()


def vote(request):
    if request.method == "POST":
        user = request.user
        if user.is_authenticated:
            movie_slug = json.loads(request.body).get('slug')
            movie = get_object_or_404(Movie, slug=movie_slug)
            vote_status = request.user.pk in Vote.objects.filter(movie=movie).values_list("user", flat=True)
            if vote_status is False:
                new_vote = Vote.objects.create(user=user, movie=movie, count=1)
                new_vote.save()
                return JsonResponse({'result': True}, safe=False)
            return JsonResponse({'result': False}, safe=False)
        return JsonResponse({'result': "user is not auth"}, safe=False)
    return JsonResponse({'result': "method is not allowed"}, safe=False)
