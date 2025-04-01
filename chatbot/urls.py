from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_home, name='chatbot_home'),  # This will handle requests to /chatbot/
    path('response/', views.chatbot_response, name='chatbot_response'),  # Handles the response from the bot
    path('set_preferences/', views.set_user_preferences, name='set_preferences'),
    path('personalized_suggestions/', views.get_personalized_suggestions, name='personalized_suggestions'),
    path('submit_feedback/<str:item_type>/<int:item_id>/', views.submit_feedback, name='submit_feedback'),
    path('feedback_success/', views.feedback_success, name='feedback_success'),
    path('preferences_success/', views.preferences_success, name='preferences_success'),
]
