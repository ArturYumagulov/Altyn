# Generated by Django 5.0.6 on 2024-09-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_city_speciality_location_is_active_region_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Населённый пункт', 'verbose_name_plural': 'Населённый пункт'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['pk'], 'verbose_name': 'Регионы', 'verbose_name_plural': 'Регион'},
        ),
        migrations.AddField(
            model_name='region',
            name='other',
            field=models.BooleanField(default=False, verbose_name='Другой'),
        ),
    ]