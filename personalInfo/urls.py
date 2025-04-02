# # In your urls.py
# # from django.urls import path
# # from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view
# # from django.urls import path
# # from .views import home_view, register_view, login_view, dashboard_view, logout_view
# # urlpatterns = [
# #     path('', home_view, name='home'),
# #     path('register/', register_view, name='register'),
# #     path('login/', login_view, name='login'),
# #     path('dashboard/', dashboard_view, name='dashboard'),
# #     path('logout/', logout_view, name='logout'),
# # ]
# from django.urls import path, include
# from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view, chatbot_home, chatbot_response

# urlpatterns = [
#     path('', home_view, name='home'),
#     path('register/', register_view, name='register'),
#     path('fitnessInformation/', fitnessInformation_view, name='fitnessInformation'),  
#     path('fitnessinformation/', fitnessInformation_view, name='fitnessinformation'),  
#     path('login/', login_view, name='login'),
#     path('dashboard/', dashboard_view, name='dashboard'),
#     path('logout/', logout_view, name='logout'),
#     path('chat/', chatbot_home, name='chatbot_home'),
#     path('chatbot/', chatbot_response, name='chatbot'),
#     path('chatbot/', include('chatbot.urls')), 
# ]


# # from django.urls import path, include
# # # from .views import home_view, register_view, fitnessInformation_view, login_view, dashboard_view, logout_view, chatbot_home
# # from personalInfo  import views

# # urlpatterns = [
# #     path('', views.home_view, name='home'),
# #     path('register/', views.register_view, name='register'),
# #     path('fitnessInformation/', views.fitnessInformation_view, name='fitnessInformation'),  
# #     path('fitnessinformation/', views.fitnessInformation_view, name='fitnessinformation'),  
# #     path('login/', views.login_view, name='login'),
# #     path('dashboard/', views.dashboard_view, name='dashboard'),
# #     path('logout/', views.logout_view, name='logout'),
# #     # path('chatbot/', chatbot, name='chatbot'),
# #     path('chatbot/', views.chatbot_home, name='chatbot'),
# #     path('chatbot/', views.chatbot_response, name='chatbot'),
# #     path('chatbot/', include('chatbot.urls')), 
# # ]


# from django.urls import path, include
# from personalInfo import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('register/', views.register_view, name='register'),
#     # path('fitnessInformation/', views.fitnessInformation_view, name='fitnessInformation'),  
#     # path('fitnessinformation/', views.fitnessInformation_view, name='fitnessinformation'),  
#     path('login/', views.login_view, name='login'),
#     path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('logout/', views.logout_view, name='logout'),
#     path('chatbot/', include('chatbot.urls')),

# ]
# from django.urls import path, include
# from personalInfo import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('logout/', views.logout_view, name='logout'),

#     # Include chatbot app URLs (this will pick up URLs defined in chatbot/urls.py)
#     path('chatbot/', include('chatbot.urls')),  # Assuming chatbot.urls.py is correctly configured
# ]

from django.urls import path, include
from  .import views  # Importing views from the personalInfo app

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),

    # User registration
    path('register/', views.register_view, name='register'),

    # Login and authentication
    path('login/', views.login_view, name='login'),

    # Dashboard page (after login)
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Logout functionality
    path('logout/', views.logout_view, name='logout'),

    # Include chatbot app URLs (assumes chatbot.urls.py is properly configured)
    path('chatbot/', include('chatbot.urls')),  # This will include the URLs from the chatbot app

    # path('fitness/', include('fitness.urls')),  # Include fitness app URLs
]
