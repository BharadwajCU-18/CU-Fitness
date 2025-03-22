# In your urls.py
<<<<<<< HEAD
from django.urls import path
import personalInfo.views as views
from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view
=======
# from django.urls import path
# from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view
>>>>>>> personalize-chatbot-responses
# from django.urls import path
# from .views import home_view, register_view, login_view, dashboard_view, logout_view
# urlpatterns = [
#     path('', home_view, name='home'),
#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
#     path('dashboard/', dashboard_view, name='dashboard'),
#     path('logout/', logout_view, name='logout'),
# ]
from django.urls import path, include
from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('fitnessInformation/', fitnessInformation_view, name='fitnessInformation'),  
    path('fitnessinformation/', fitnessInformation_view, name='fitnessinformation'),  
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
<<<<<<< HEAD
    path('chat/', chatbot_home, name='chatbot_home'),
    path('chatbot/', chatbot_response, name='chatbot'),
    path('generate_report/', views.generate_report, name='generate_report'),
=======
    # path('chat/', chatbot_home, name='chatbot_home'),
    # path('chatbot/', chatbot_response, name='chatbot'),
    path('chatbot/', include('chatbot.urls')), 
>>>>>>> personalize-chatbot-responses
]


