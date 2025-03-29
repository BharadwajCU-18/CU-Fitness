from django.db import models
import datetime

class FitnessReport(models.Model):
    date = models.DateField(default=datetime.date.today)
    steps = models.IntegerField(default=0)
    cardio_time = models.IntegerField(default=0)  # In minutes
    cool_down_time = models.IntegerField(default=0)  # In minutes

    def __str__(self):
        return f"Progress for {self.date}"