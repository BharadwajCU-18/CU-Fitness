# from django import forms
# from .models import FitnessReport

# class FitnessForm(forms.ModelForm):
#     class Meta:
#         model = FitnessReport
#         fields = ['pull_ups', 'cardio_time', 'cool_down_time', 'hours_of_sleep']

from django import forms
from .models import FitnessReport  # Ensure the model is imported correctly

class FitnessForm(forms.ModelForm):
    class Meta:
        model = FitnessReport  # Make sure this is your actual model
        fields = ['pull_ups', 'cardio_time', 'cool_down_time', 'hours_of_sleep']
