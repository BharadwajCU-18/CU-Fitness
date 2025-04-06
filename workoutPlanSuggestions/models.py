from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    FITNESS_GOALS = [
        ('build_muscle', 'Build Muscle'),
        ('lose_weight', 'Lose Weight'),
        ('increase_stamina', 'Increase Stamina'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    fitness_goal = models.CharField(max_length=50, choices=FITNESS_GOALS)
    sets = models.PositiveIntegerField(default=3)
    reps = models.CharField(max_length=20, default="8-12")
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class RecommendationFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_recommendation_feedback")
    title = models.CharField(max_length=255, default="Overall Recommendation")
    rating = models.PositiveSmallIntegerField(help_text="Rate from 1 (worst) to 5 (best)")
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title} Rating: {self.rating}"

class SavedWorkoutPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan_html = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
