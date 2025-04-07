# """
# URL configuration for CU_Fitness project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('personalInfo.urls')),
#     #  path('registration/', include('registration.urls')),

# ]
from django.contrib import admin
from django.urls import path, include
# from personalInfo.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personalInfo.urls')),
    path('chatbot/', include('chatbot.urls')),  # Include chatbot app URLs
    path('mealSuggestions/', include('mealSuggestions.urls')),  # Include mealSuggestions app URLs
    path('home/', include('home.urls')),  # Include home app URLs
    path('payment/', include('payment.urls')),  # Include payment app URLs
    path('profiles/', include('profiles.urls')),  # Include profiles app URLs
    path('workoutPlanSuggestions/', include('workoutPlanSuggestions.urls')),  # Include workoutPlanSuggestions app URLs
    path('fitnessProgress/', include('fitnessProgress.urls')),  # Include fitnessProgress app URLs
    path('fitnessReport/', include('fitnessReport.urls')),  # Include fitnessReport app URLs
    
] 