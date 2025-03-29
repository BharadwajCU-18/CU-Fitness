



from django.urls import path
import fitness.views as views
# from . import views

from .views import fitness_dashboard, fitness_report_chart

urlpatterns = [
    path('fitness_dashboard/', fitness_dashboard, name='fitness_dashboard'),
    path('fitness_report_chart/', fitness_report_chart, name='fitness_report_chart'),
]