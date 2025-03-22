from django.urls import path
from . import views

urlpatterns = [
    path('set_preferences/', views.set_user_preferences, name='set_preferences'),
    path('personalized_suggestions/', views.get_personalized_suggestions, name='personalized_suggestions'),
    path('submit_feedback/<str:item_type>/<int:item_id>/', views.submit_feedback, name='submit_feedback'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('preferences_success/', views.preferences_success, name='preferences_success'),
]
