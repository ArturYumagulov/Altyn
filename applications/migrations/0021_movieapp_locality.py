# Generated by Django 5.0.6 on 2024-10-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0020_alter_movieapp_contract"),
    ]

    operations = [
        migrations.AddField(
            model_name="movieapp",
            name="locality",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=2000,
                null=True,
                verbose_name="Населенный пункт",
            ),
        ),
    ]