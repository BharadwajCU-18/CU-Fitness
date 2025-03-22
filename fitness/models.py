from django.db import models

class FitnessReport(models.Model):
    pull_ups = models.PositiveIntegerField()
    cardio_time = models.PositiveIntegerField(help_text="Time in minutes")
    cool_down_time = models.PositiveIntegerField(help_text="Time in minutes")
    hours_of_sleep = models.PositiveIntegerField()

    def __str__(self):
        return f"Fitness Report - {self.id}"

    def calculate_calories_burned(self):
        
        calories_from_pullups = self.pull_ups * 0.25  
        calories_from_cardio = self.cardio_time * 8
        calories_from_cool_down = self.cool_down_time * 2  
        calories_from_sleep = self.hours_of_sleep * 50

        total_calories = calories_from_pullups + calories_from_cardio + calories_from_cool_down + calories_from_sleep
        return total_calories

    def __str__(self):
        return f"Fitness Report - Calories Burned: {self.calculate_calories_burned()}"

