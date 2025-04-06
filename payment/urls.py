
from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.payment_view, name='subscribe'),
]
