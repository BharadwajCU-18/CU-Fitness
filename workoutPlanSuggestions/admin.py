from django.contrib import admin
from workoutPlanSuggestions.models import Workout, RecommendationFeedback

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "fitness_goal", "sets", "reps", "instructions")

admin.site.register(RecommendationFeedback)
