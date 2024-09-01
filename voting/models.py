from django.db import models

from movies.models import Movie
from users.models import CustomUser


# Create your models here.


class Voting(models.Model):

    is_active = models.BooleanField(default=False, verbose_name="Голосование")
    name = models.CharField(max_length=300, verbose_name="Название")
    start = models.DateField(verbose_name="Начало")
    end = models.DateField(verbose_name="Конец")
    movies = models.ManyToManyField(Movie, related_name='movies')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Голосование"
        verbose_name_plural = "Голосования"


class VoteItem(models.Model):

    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

