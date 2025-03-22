from django.db import models

class FitnessReport(models.Model):
    pull_ups = models.PositiveIntegerField()
    cardio_time = models.PositiveIntegerField(help_text="Time in minutes")
    cool_down_time = models.PositiveIntegerField(help_text="Time in minutes")
    hours_of_sleep = models.PositiveIntegerField()

    def __str__(self):
        return f"Fitness Report - {self.id}"

    def calculate_calories_burned(self):
        # Assuming an average calorie burn estimation for each activity:
        calories_from_pullups = self.pull_ups * 0.25  # 0.25 calories per pull-up
        calories_from_cardio = self.cardio_time * 8  # 8 calories per minute for cardio
        calories_from_cool_down = self.cool_down_time * 2  # 2 calories per minute for cool down
        calories_from_sleep = self.hours_of_sleep * 50  # 50 calories per hour of sleep (estimate)

        total_calories = calories_from_pullups + calories_from_cardio + calories_from_cool_down + calories_from_sleep
        return total_calories

    def __str__(self):
        return f"Fitness Report - Calories Burned: {self.calculate_calories_burned()}"

