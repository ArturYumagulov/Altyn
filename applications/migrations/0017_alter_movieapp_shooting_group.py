# Generated by Django 5.0.6 on 2024-10-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0016_mainshootinggroup_shootinggroupspecialist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieapp',
            name='shooting_group',
            field=models.ManyToManyField(to='applications.mainshootinggroup'),
        ),
    ]
