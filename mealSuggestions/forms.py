from django import forms

class MealPreferencesForm(forms.Form):
    # Choices for dietary restrictions, fitness goals, and meal preferences
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

    # Form fields
    dietary_restrictions = forms.ChoiceField(choices=DIETARY_CHOICES, required=True)
    fitness_goals = forms.ChoiceField(choices=FITNESS_GOALS, required=True)
    meal_preferences = forms.ChoiceField(choices=MEAL_PREFERENCES, required=True)

    # Optional fields for additional flexibility (can be used for future extensions)
    TIME_AVAILABILITY = [
        ('10_min', '10 min'),
        ('20_min', '20 min'),
        ('30_min', '30 min+'),
    ]
    time_availability = forms.ChoiceField(choices=TIME_AVAILABILITY, required=True)

    # Budget for the meal preferences
    budget = forms.DecimalField(decimal_places=2, required=True)

class RecommendationFeedbackForm(forms.Form):
    # Choices for rating
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Rating from 1 to 5
    
    # Form fields for rating and comments
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, required=True)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}), required=False)

    # Hidden field to store the meal's name when submitting feedback
    meal_name = forms.CharField(widget=forms.HiddenInput(), required=True)
