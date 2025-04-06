# from django.urls import path
# from . import views

# # Define app_name to namespace your URLs
# app_name = 'profiles'

# urlpatterns = [
#     path('my-profile/', views.my_profile, name='profile'),  # Use the 'profile' name for the URL pattern
# ]


from django.urls import path

from . import views
 
urlpatterns = [

     path('update_fitness_profile/', views.update_fitness_profile, name='update_fitness_profile'),

     path('profile/', views.profile_view, name='profile'),

 ]