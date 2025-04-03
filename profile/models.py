from django.db import models

# Create your models here.
from django.contrib.auth.models import User

ACTIVITY_LEVELS = [
    ('Sedentary', 'Sedentary'),
    ('Light', 'Light Activity'),
    ('Moderate', 'Moderate Activity'),
    ('Intense', 'Intense Activity'),
]

FITNESS_GOALS = [
    ('Weight Loss', 'Weight Loss'),
    ('Strength Building', 'Strength Building'),
    ('Endurance', 'Endurance'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_LEVELS, blank=True)
    fitness_goal = models.CharField(max_length=20, choices=FITNESS_GOALS, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
