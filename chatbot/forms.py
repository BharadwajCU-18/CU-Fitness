from django import forms
from .models import UserPreferences

# Form for capturing user preferences
class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['preferred_workout_type', 'preferred_meal_type', 'dietary_restrictions', 'fitness_goal']
