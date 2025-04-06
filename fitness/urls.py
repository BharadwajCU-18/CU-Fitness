# from django.urls import path
# import fitness.views as views
# # from . import views
# from django.contrib.auth.decorators import login_required

# from .views import fitness_dashboard, fitness_report_chart

# urlpatterns = [
#     path('fitness_dashboard/', login_required(fitness_dashboard), name='fitness_dashboard'),
#     path('fitness_report_chart/', login_required(fitness_report_chart), name='fitness_report_chart'),
# ]

from django.urls import path
from .views import fitness_dashboard, fitness_report_chart

urlpatterns = [
    path('fitness_dashboard/', fitness_dashboard, name='fitness_dashboard'),
    path('report_chart/', fitness_report_chart, name='fitness_report_chart'),
]
