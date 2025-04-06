from django.contrib.auth.models import User
from django.db import models

class FitnessInformation(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dietary_preferences = models.CharField(max_length=100, null=True, blank=True)
    fitness_goals = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Fitness Info for {self.user.username}"

