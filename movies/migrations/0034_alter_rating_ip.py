# Generated by Django 5.0.6 on 2024-10-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0033_movie_artistical_director_movie_costumer_designer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="ip",
            field=models.CharField(max_length=15, verbose_name="IP"),
        ),
    ]
