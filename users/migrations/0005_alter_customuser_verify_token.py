# Generated by Django 5.0.6 on 2024-10-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_customuser_verify_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="verify_token",
            field=models.CharField(
                blank=True,
                default="c7236cc8d73457d9f95411f5b3c4a8444f7606e8",
                max_length=40,
                null=True,
            ),
        ),
    ]
