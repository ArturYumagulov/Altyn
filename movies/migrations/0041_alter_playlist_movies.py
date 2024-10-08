# Generated by Django 5.0.6 on 2024-10-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0040_playlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playlist",
            name="movies",
            field=models.ManyToManyField(
                blank=True,
                related_name="playlists",
                to="movies.movie",
                verbose_name="Фильмы в плейлисте",
            ),
        ),
    ]
