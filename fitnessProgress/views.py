from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkoutEntryForm

@login_required
def log_workout(request):
    if request.method == 'POST':
        form = WorkoutEntryForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('fitness_progress')
    else:
        form = WorkoutEntryForm()
    return render(request, 'fitnessProgress.html', {'form': form})
