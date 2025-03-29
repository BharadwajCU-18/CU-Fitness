from django import forms
from .models import FitnessReport

class FitnessProgressForm(forms.ModelForm):
    class Meta:
        model = FitnessReport
        fields = ['date', 'steps', 'cardio_time', 'cool_down_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
