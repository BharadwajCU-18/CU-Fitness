from django.contrib import admin
from mealSuggestions.models import Meal, FavoriteMeal

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
admin.site.register(FavoriteMeal)  # Register the FavoriteMeal model with the admin site.














