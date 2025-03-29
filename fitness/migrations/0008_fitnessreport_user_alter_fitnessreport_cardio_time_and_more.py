# Generated by Django 5.1.7 on 2025-03-29 05:56

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitness", "0007_remove_fitnessreport_user_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="fitnessreport",
            name="user",
            field=models.ForeignKey(
                default=datetime.datetime.now,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="fitnessreport",
            name="cardio_time",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="fitnessreport",
            name="cool_down_time",
            field=models.FloatField(default=0),
        ),
    ]
