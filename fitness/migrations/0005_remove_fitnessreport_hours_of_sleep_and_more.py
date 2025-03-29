# Generated by Django 5.1.7 on 2025-03-28 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fitness", "0004_alter_fitnessreport_cardio_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fitnessreport",
            name="hours_of_sleep",
        ),
        migrations.RemoveField(
            model_name="fitnessreport",
            name="pull_ups",
        ),
        migrations.AddField(
            model_name="fitnessreport",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="fitnessreport",
            name="steps",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="fitnessreport",
            name="cardio_time",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="fitnessreport",
            name="cool_down_time",
            field=models.IntegerField(default=0),
        ),
    ]
