# Generated by Django 5.0.6 on 2024-09-30 18:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0013_alter_almanach_options_remove_almanach_main_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="almanach",
            name="created_date",
            field=models.DateField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="almanach",
            name="edit_date",
            field=models.DateField(auto_now=True, verbose_name="Дата изменения"),
        ),
    ]
