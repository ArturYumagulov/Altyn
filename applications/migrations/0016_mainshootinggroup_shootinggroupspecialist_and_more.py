# Generated by Django 5.0.6 on 2024-09-21 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_alter_specialistapp_speciality'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShootingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('birthday', models.DateField(blank=True, default=None, null=True, verbose_name='Дата рождения')),
                ('biography', models.TextField(blank=True, default=None, null=True, verbose_name='Биография')),
            ],
        ),
        migrations.CreateModel(
            name='ShootingGroupSpecialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование специальности')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Специалист съемочной группы',
                'verbose_name_plural': 'Специалист съемочной группы',
            },
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='scenarist',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='artistical_director_first_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='artistical_director_last_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='compositor_first_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='compositor_last_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='costume_designer_first_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='costume_designer_last_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='operator_first_name',
        ),
        migrations.RemoveField(
            model_name='movieapp',
            name='operator_last_name',
        ),
        migrations.AddField(
            model_name='movieapp',
            name='shooting_group',
            field=models.ManyToManyField(default=None, null=True, to='applications.mainshootinggroup'),
        ),
        migrations.AddField(
            model_name='mainshootinggroup',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='applications.shootinggroupspecialist'),
        ),
        migrations.DeleteModel(
            name='AppDirector',
        ),
        migrations.DeleteModel(
            name='AppProducer',
        ),
        migrations.DeleteModel(
            name='AppScenarist',
        ),
    ]
