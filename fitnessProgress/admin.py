from django.contrib import admin
from .models import WorkoutEntry

@admin.register(WorkoutEntry)
class WorkoutEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'exercise_name', 'sets', 'reps')
    list_filter = ('date', 'user')
    search_fields = ('exercise_name', 'user__username')
