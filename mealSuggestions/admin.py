from django.contrib import admin
<<<<<<< HEAD
from mealSuggestions.models import Meal, FavoriteMeal, RecommendationFeedback
=======
from mealSuggestions.models import Meal, FavoriteMeal
>>>>>>> origin/main

# Register your models here.
# admin.site.register(Meal)  # Register the Meal model with the admin site.
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "fitness_goals",
        "dietary_restrictions",
        "meal_type",
        "time_required",  # This is your "Time availability"
        "budget",
    )
<<<<<<< HEAD
admin.site.register(FavoriteMeal)  # Register the FavoriteMeal model with the admin site.
admin.site.register(RecommendationFeedback)  # Register the RecommendationFeedback model with the admin site.
=======
admin.site.register(FavoriteMeal)  # Register the FavoriteMeal model with the admin site.
>>>>>>> origin/main
