# In your urls.py
from django.urls import path
import personalInfo.views as views
from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('fitnessInformation/', fitnessInformation_view, name='fitnessInformation'),  # Update to camel case
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('generate_report/', views.generate_report, name='generate_report'),
]


