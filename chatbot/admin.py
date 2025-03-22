from django.contrib import admin
from .models import UserPreferences, Workout, Meal, Feedback

admin.site.register(UserPreferences)
admin.site.register(Workout)
admin.site.register(Meal)
admin.site.register(Feedback)
