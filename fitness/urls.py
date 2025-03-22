from django.urls import path
import fitness.views as views
from . import views

urlpatterns = [
    path('fitness/', views.fitness_dashboard, name='fitness_dashboard'),
]



