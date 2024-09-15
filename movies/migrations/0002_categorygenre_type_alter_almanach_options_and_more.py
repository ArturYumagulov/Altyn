# Generated by Django 5.0.6 on 2024-09-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Жанр вида',
                'verbose_name_plural': 'Жанр вида',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('name', models.CharField(max_length=500, verbose_name='Наименование')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Вид',
            },
        ),
        migrations.AlterModelOptions(
            name='almanach',
            options={'ordering': ['name'], 'verbose_name': 'Альмонах', 'verbose_name_plural': 'Альмонахи'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['pk'], 'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.AddField(
            model_name='movie',
            name='debut',
            field=models.BooleanField(default=False, verbose_name='Дебютный'),
        ),
        migrations.AddField(
            model_name='movie',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
    ]