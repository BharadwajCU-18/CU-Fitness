# Generated by Django 5.2 on 2025-04-06 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitnessProgress", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workoutentry",
            name="calories_burned",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
