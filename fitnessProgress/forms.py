from django import forms
from .models import WorkoutEntry

class WorkoutEntryForm(forms.ModelForm):
    class Meta:
        model = WorkoutEntry
        fields = ['date', 'exercise_name', 'sets', 'reps']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
