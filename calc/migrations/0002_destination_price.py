# Generated by Django 5.1.5 on 2025-01-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calc", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="destination",
            name="price",
            field=models.IntegerField(default=0.0),
        ),
    ]
