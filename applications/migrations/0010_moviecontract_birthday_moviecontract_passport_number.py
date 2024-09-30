# Generated by Django 5.0.6 on 2024-09-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_moviecontract_created_date_moviecontract_edit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecontract',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='moviecontract',
            name='passport_number',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Номер паспорта'),
        ),
    ]