from django.db import models
from django.contrib.auth.models import User

class WorkoutEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise_name = models.CharField(max_length=255)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.exercise_name} on {self.date}"
    


