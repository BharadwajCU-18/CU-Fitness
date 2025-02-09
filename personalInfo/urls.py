from django.urls import path
from . import views

urlpatterns = [
    path('personalInfo/', views.personalInfo, name='personalInfo'),
    path('FitnessInfo/', views.FitnessInformation, name='FitnessInfo'),
]