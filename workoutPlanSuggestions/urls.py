from django.urls import path
from .views import submit_workout_preferences, submit_feedback

urlpatterns = [
    path('submit_workout_preferences/', submit_workout_preferences, name='submit_workout_preferences'),
    # path('submit_feedback/', submit_feedback, name='submit_feedback'),
    path('submit_feedback/', submit_feedback, name='workout_feedback')
]
