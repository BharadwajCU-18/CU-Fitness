# Generated by Django 5.2 on 2025-04-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalInfo", "0010_alter_fitnessinformation_dietary_preferences_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fitnessinformation",
            name="phone_number",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
