# Generated by Django 5.1.7 on 2025-03-27 04:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealSuggestions', '0002_recommendationfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendationfeedback',
            name='meal_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommendationfeedback',
            name='rating',
            field=models.PositiveSmallIntegerField(help_text='Rate from 1 (worst) to 5 (best)'),
        ),
    ]
