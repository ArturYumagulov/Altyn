# Generated by Django 5.0.6 on 2024-09-11 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rollercertificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='agelimit',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rolled_certificate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.rollercertificate', verbose_name='Прокатное удостоверение'),
        ),
    ]
