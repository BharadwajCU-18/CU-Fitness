# from django import forms
# from .models import FitnessReport

# class FitnessProgressForm(forms.ModelForm):
#     class Meta:
#         model = FitnessReport
#         fields = ['date', 'steps', 'cardio_time', 'cool_down_time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }


# from django import forms
# from .models import FitnessReport

# class FitnessProgressForm(forms.ModelForm):
#     class Meta:
#         model = FitnessReport
#         fields = ['date', 'steps', 'cardio_time', 'cool_down_time']
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#         }


from django import forms
from .models import FitnessReport

class FitnessProgressForm(forms.ModelForm):
    class Meta:
        model = FitnessReport
        fields = ['date', 'steps', 'cardio_time', 'cool_down_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_steps(self):
        steps = self.cleaned_data.get('steps')
        if steps < 0:
            raise forms.ValidationError('Steps cannot be negative.')
        return steps

    def clean_cardio_time(self):
        cardio_time = self.cleaned_data.get('cardio_time')
        if cardio_time < 0:
            raise forms.ValidationError('Cardio time cannot be negative.')
        return cardio_time

    def clean_cool_down_time(self):
        cool_down_time = self.cleaned_data.get('cool_down_time')
        if cool_down_time < 0:
            raise forms.ValidationError('Cool down time cannot be negative.')
        return cool_down_time
