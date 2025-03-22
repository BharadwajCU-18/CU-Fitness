from django.db import models
from django.contrib.auth.models import User  # Import User model

class Meal(models.Model):
    DIETARY_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('gluten_free', 'Gluten-Free'),
        ('dairy_free', 'Dairy-Free'),
        ('none', 'No Restrictions'),
    ]

    FITNESS_GOALS = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('energy_boost', 'Energy Boost'),
    ]

    MEAL_PREFERENCES = [
        ('quick_meals', 'Quick Meals'),
        ('high_protein', 'High-Protein'),
        ('low_carb', 'Low-Carb'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    dietary_restrictions = models.CharField(max_length=50, choices=DIETARY_CHOICES)
    fitness_goals = models.CharField(max_length=50, choices=FITNESS_GOALS)
    meal_type = models.CharField(max_length=50, choices=MEAL_PREFERENCES)
    time_required = models.IntegerField(help_text="Time required in minutes")
    budget = models.DecimalField(max_digits=5, decimal_places=2, help_text="Cost in CAD")
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.budget} CAD"

class FavoriteMeal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'meal')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} - {self.meal.name}"
