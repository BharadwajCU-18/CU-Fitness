from django.db import models
from django.contrib.auth.models import User

# Model for storing User Preferences
class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_workout_type = models.CharField(
        max_length=100,
        choices=[('strength', 'Strength'), ('cardio', 'Cardio'), ('core', 'Core'), ('flexibility', 'Flexibility')],
        null=True,
        blank=True
    )
    preferred_meal_type = models.CharField(
        max_length=100,
        choices=[('protein', 'Protein'), ('carb', 'Carb'), ('fat', 'Fat'), ('vegan', 'Vegan')],
        null=True,
        blank=True
    )
    dietary_restrictions = models.TextField(null=True, blank=True)  # e.g., "Gluten-Free"
    fitness_goal = models.CharField(
        max_length=100,
        choices=[('weight_loss', 'Weight Loss'), ('muscle_gain', 'Muscle Gain'), ('maintain', 'Maintain Weight')],
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Preferences for {self.user.username}"

# Model for storing Workout details
class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=[('strength', 'Strength'), ('cardio', 'Cardio'), ('core', 'Core'), ('flexibility', 'Flexibility')],
    )
    duration_minutes = models.IntegerField()  # Duration in minutes

    def __str__(self):
        return self.name

# Model for storing Meal details
class Meal(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=[('protein', 'Protein'), ('carb', 'Carb'), ('fat', 'Fat'), ('vegan', 'Vegan')],
    )
    calories = models.IntegerField()  # Calories per serving

    def __str__(self):
        return self.name

# Model for storing Feedback from users
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} on {self.workout.name if self.workout else self.meal.name}"
    
