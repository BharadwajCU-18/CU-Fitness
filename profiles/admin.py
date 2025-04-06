from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FitnessProfile

@admin.register(FitnessProfile)
class FitnessProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'age', 'height', 'weight')