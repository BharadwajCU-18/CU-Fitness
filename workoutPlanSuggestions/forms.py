from django import forms

class WorkoutPreferencesForm(forms.Form):
    FITNESS_GOALS = [
        ('build_muscle', 'Build Muscle'),
        ('lose_weight', 'Lose Weight'),
        ('increase_stamina', 'Increase Stamina'),
    ]
    AVAILABLE_DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    fitness_goal = forms.ChoiceField(choices=FITNESS_GOALS, required=True)
    available_days = forms.MultipleChoiceField(
        choices=AVAILABLE_DAYS,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

class OverallFeedbackForm(forms.Form):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect, required=True)
    comments = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        required=False
    )
