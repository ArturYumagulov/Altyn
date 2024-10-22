from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from movies.models import Movie

User = get_user_model()

# Create your models here.


class Voting(models.Model):
    """Модель голосования"""

    name = models.CharField(max_length=2000, verbose_name="Наименование")
    movies = models.ManyToManyField(Movie, verbose_name="Фильмы", related_name="voting_movies")
    start_date = models.DateTimeField(verbose_name="Дата начала голосования", blank=True, null=True, default=None)
    end_date = models.DateTimeField(verbose_name="Дата окончания голосования", blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", blank=True, null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.name} с {self.start_date} до {self.end_date}"

    def is_active(self):
        """Проверяет, активно ли голосование в зависимости от текущей даты"""
        now = timezone.now()
        return self.start_date <= now <= self.end_date

    class Meta:
        verbose_name = "Голосование"
        verbose_name_plural = "Голосование"


class Vote(models.Model):
    """Голосование"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='votes')
    count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('movie', 'user')
        verbose_name = "Голос"
        verbose_name_plural = "Голоса"

    def __str__(self):
        return f"{self.user} проголосовал за {self.movie}"


