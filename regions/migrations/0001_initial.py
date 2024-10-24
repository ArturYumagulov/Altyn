# Generated by Django 5.0.6 on 2024-07-06 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Регионы',
                'verbose_name_plural': 'Регион',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regions.region')),
            ],
            options={
                'verbose_name': 'Локации',
                'verbose_name_plural': 'Локация',
            },
        ),
    ]
