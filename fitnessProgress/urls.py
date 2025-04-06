from django.urls import path
from .views import log_workout

urlpatterns = [
    path('fitness_progress/', log_workout, name='fitness_progress'),
]
