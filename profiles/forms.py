# from django import forms
# from .models import FitnessProfile

# class FitnessInformationForm(forms.ModelForm):
#     class Meta:
#         model = FitnessProfile
#         fields = [
#             'phone_number',
#             'age',
#             'height',
#             'weight',
#             'dietary_preferences',
#             'fitness_goals',
#         ]

from django import forms

from .models import FitnessProfile
 
class FitnessInformationForm(forms.ModelForm):

     class Meta:

         model = FitnessProfile

         fields = [

             'phone_number',

             'age',

             'height',

             'weight',

             'dietary_preferences',

             'fitness_goals',

         ]