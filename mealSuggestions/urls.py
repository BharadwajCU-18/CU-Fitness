from django.urls import path
from .views import submit_meal_preferences, add_to_favorites

urlpatterns = [
    path('submit_meal_preferences/', submit_meal_preferences, name='submit_meal_preferences'),
    path('add_to_favorites/<int:meal_id>/', add_to_favorites, name='add_to_favorites'),
]
