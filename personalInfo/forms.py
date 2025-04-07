from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FitnessInformation
# from .models import CommunityPost

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
        ]

class FitnessInformationForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        label='Phone Number',
        error_messages={'required': 'Phone Number is required'}
     )
    age = forms.IntegerField(
        required=True,
        min_value=1,
        label='Age',
        error_messages={'required': 'Age is required'}
    )
    height = forms.FloatField(
        required=True,
        min_value=1,
        label='Height (in cm)',
        error_messages={'required': 'Height is required'}
    )
    weight = forms.FloatField(
        required=True,
        min_value=1,
        label='Weight (in kg)',
        error_messages={'required': 'Weight is required'}
    )
    dietary_preferences = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        required=True,
        label='Dietary Preferences',
        error_messages={'required': 'Dietary Preferences are required'}
    )
    fitness_goals = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}),
        required=True,
        label='Fitness Goals',
        error_messages={'required': 'Fitness Goals are required'}
    )

    class Meta:
        model = FitnessInformation
        fields = ['phone_number','age', 'height', 'weight', 'dietary_preferences', 'fitness_goals']

