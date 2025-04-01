from django.urls import path
<<<<<<< HEAD
from .views import submit_meal_preferences, add_to_favorites, delete_favorite, submit_feedback
=======
from .views import submit_meal_preferences, add_to_favorites
>>>>>>> origin/main

urlpatterns = [
    path('submit_meal_preferences/', submit_meal_preferences, name='submit_meal_preferences'),
    path('add_to_favorites/<int:meal_id>/', add_to_favorites, name='add_to_favorites'),
<<<<<<< HEAD
    path('delete_favorite/<int:favorite_id>/', delete_favorite, name='delete_favorite'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),

=======
>>>>>>> origin/main
]
