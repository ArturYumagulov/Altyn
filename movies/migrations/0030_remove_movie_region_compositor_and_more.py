# Generated by Django 5.0.6 on 2024-10-05 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0029_mainshootinggroup_shootinggroupspecialist_and_more'),
        ('regions', '0005_compositor_director_operator_producer_scenarist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='region_compositor',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='region_director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='region_operator',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='region_producer',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='region_scenarist',
        ),
        migrations.AlterField(
            model_name='movie',
            name='compositor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='regions.compositor', verbose_name='Композитор-регион'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AlterField(
            model_name='movie',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='regions.operator', verbose_name='Оператор'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='scenarist',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='directors', to='regions.director', verbose_name='Режиссеры'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.ManyToManyField(blank=True, related_name='producers', to='regions.producer', verbose_name='Продюссеры-регион'),
        ),
        migrations.AddField(
            model_name='movie',
            name='scenarist',
            field=models.ManyToManyField(blank=True, related_name='scenarists', to='regions.scenarist', verbose_name='Сценарист-регион'),
        ),
    ]
