# Generated by Django 5.0.6 on 2024-10-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_verify_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='verify_token',
            field=models.CharField(blank=True, default='79447cb0e83099c6ca9d790b080ea86b38385292589ac78bb52d2e206b150f14b8d5da0a0109f32a', max_length=40, null=True),
        ),
    ]