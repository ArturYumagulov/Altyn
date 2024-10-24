# Generated by Django 5.0.6 on 2024-10-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_movie_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, null=True, related_name='directors', to='movies.director', verbose_name='Режиссер'),
        ),
    ]
