# Generated by Django 5.0.6 on 2024-09-17 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_delete_region_alter_movie_region'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='MovieStatus',
        ),
    ]