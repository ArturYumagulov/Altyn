# Generated by Django 5.0.6 on 2024-10-09 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("regions", "0007_artisticaldirector_costumerdesigner"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScreeningPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Активность"),
                ),
                ("name", models.CharField(max_length=500, verbose_name="Название")),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "social_net",
                    models.CharField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Ссылка на соцсеть",
                    ),
                ),
                (
                    "site",
                    models.CharField(
                        blank=True, max_length=2000, null=True, verbose_name="Сайт"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=2000, null=True, verbose_name="Сайт"
                    ),
                ),
                ("image", models.ImageField(upload_to="regions/screening_points/")),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="regions.region",
                        verbose_name="Регион",
                    ),
                ),
            ],
            options={
                "verbose_name": "Точка кинопоказа",
                "verbose_name_plural": "Точки кинопоказа",
                "ordering": ["pk"],
            },
        ),
    ]