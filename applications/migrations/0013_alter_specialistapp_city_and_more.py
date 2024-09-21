# Generated by Django 5.0.6 on 2024-09-18 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_alter_specialistapp_portfolio'),
        ('regions', '0004_remove_specialist_status_remove_specialist_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialistapp',
            name='city',
            field=models.CharField(default=None, max_length=1000, null=True, verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='descriptions',
            field=models.TextField(default=None, null=True, verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='email',
            field=models.EmailField(default=None, max_length=225, null=True, verbose_name='Электронный адрес'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='phone',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='region',
            field=models.ManyToManyField(default=None, null=True, to='regions.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='social_link',
            field=models.TextField(default=None, null=True, verbose_name='Ссылка на социальные сети'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='speciality',
            field=models.ManyToManyField(default=None, null=True, related_name='app_specialities', to='regions.speciality'),
        ),
        migrations.AlterField(
            model_name='specialistapp',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='applications.status', verbose_name='Статус'),
        ),
    ]
