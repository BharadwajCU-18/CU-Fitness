from django.db import models
from django.contrib.auth.models import User

class FitnessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dietary_preferences = models.TextField(null=True, blank=True)
    fitness_goals = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Fitness Profile"
