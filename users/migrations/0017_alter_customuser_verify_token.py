# Generated by Django 5.0.6 on 2024-10-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_alter_customuser_verify_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="verify_token",
            field=models.CharField(
                blank=True,
                default="801b48d9822912fc201000516b724ba0ebb0c7da1cd3ebcfb20b9b922d21a77c67bcf63554358240",
                max_length=40,
                null=True,
            ),
        ),
    ]
