from django.urls import path
from .views import fitness_report

urlpatterns = [
    path('fitness_report/', fitness_report, name='fitness_report'),
]
