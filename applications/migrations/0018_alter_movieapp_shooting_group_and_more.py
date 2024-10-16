# Generated by Django 5.0.6 on 2024-10-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0017_alter_movieapp_shooting_group'),
        ('movies', '0029_mainshootinggroup_shootinggroupspecialist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieapp',
            name='shooting_group',
            field=models.ManyToManyField(to='movies.mainshootinggroup'),
        ),
        migrations.DeleteModel(
            name='MainShootingGroup',
        ),
        migrations.DeleteModel(
            name='ShootingGroupSpecialist',
        ),
    ]
