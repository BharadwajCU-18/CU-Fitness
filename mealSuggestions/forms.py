from django import forms

class MealPreferencesForm(forms.Form):
    DIETARY_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('gluten_free', 'Gluten-Free'),
        ('dairy_free', 'Dairy-Free'),
        ('none', 'No Restrictions'),
    ]

    FITNESS_GOALS = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('energy_boost', 'Energy Boost'),
    ]

    MEAL_PREFERENCES = [
        ('quick_meals', 'Quick Meals'),
        ('high_protein', 'High-Protein'),
        ('low_carb', 'Low-Carb'),
        ('no_preferences', 'No Meal Preferences'),
    ]

<<<<<<< HEAD
    dietary_restrictions = forms.ChoiceField(choices=DIETARY_CHOICES, required=True)
    fitness_goals = forms.ChoiceField(choices=FITNESS_GOALS, required=True)
    meal_preferences = forms.ChoiceField(choices=MEAL_PREFERENCES, required=True)

# class RecommendationFeedbackForm(forms.Form):
#     # The meal_name is passed via a hidden input so it's not included here.
#     RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
#     rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, required=True)
#     comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), required=False)
class RecommendationFeedbackForm(forms.Form):
    pass
=======
    TIME_AVAILABILITY = [
        ('10_min', '10 min'),
        ('20_min', '20 min'),
        ('30_min', '30 min+'),
    ]

    dietary_restrictions = forms.ChoiceField(choices=DIETARY_CHOICES, required=True)
    fitness_goals = forms.ChoiceField(choices=FITNESS_GOALS, required=True)
    meal_preferences = forms.ChoiceField(choices=MEAL_PREFERENCES, required=True)
    time_availability = forms.ChoiceField(choices=TIME_AVAILABILITY, required=True)
    budget = forms.DecimalField(decimal_places=2, required=True)
>>>>>>> origin/main
