# Generated by Django 5.0.6 on 2024-09-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_verify_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='verify_token',
            field=models.CharField(blank=True, default='889b238ef61349960f4f94a1ff23c7e839778c5d0509cc7fb3ebabbf42a6b05d80bb5c3e01004ece', max_length=40, null=True),
        ),
    ]