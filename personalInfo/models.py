from django.db import models

# Create your models here.

# personalInfo/models.py
from django.db import models

class FitnessInformation(models.Model):
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    dietary_preferences = models.CharField(max_length=100)
    fitness_goals = models.CharField(max_length=100)

    def __str__(self):
        return f"Fitness Info: {self.age} years old"
