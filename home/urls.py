from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('submit-community-post/', views.submit_community_post, name='submit_community_post'),
]
