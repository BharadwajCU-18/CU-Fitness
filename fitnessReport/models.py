from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Workoutreport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise_name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.date} - {self.exercise_name}"

    class Meta:
        verbose_name_plural = "Workout Entries"

    def calories_burned(self):
        # Simple formula: 0.1 calories per rep
        return self.sets * self.reps * 0.1

