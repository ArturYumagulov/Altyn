# Generated by Django 5.0.6 on 2024-09-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_genre_group_1_genre_group_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='RollerCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Прокатное удостоверение',
                'verbose_name_plural': 'Прокатное удостоверение',
            },
        ),
    ]
