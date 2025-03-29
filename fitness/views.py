from django.shortcuts import render, redirect
from .forms import FitnessProgressForm

from .models import FitnessReport

def fitness_dashboard(request):
    if request.method == 'POST':
        form = FitnessProgressForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('fitness_dashboard')  # Redirect back to the form page
    else:
        form = FitnessProgressForm()

    return render(request, 'fitness/dashboard.html', {'form': form})


# views.py


def fitness_report_chart(request):
    # Get the data from the database
    fitness_reports = FitnessReport.objects.all()
    dates = [report.date.strftime('%Y-%m-%d') for report in fitness_reports]
    steps = [report.steps for report in fitness_reports]
    cardio_time = [report.cardio_time for report in fitness_reports]
    cool_down_time = [report.cool_down_time for report in fitness_reports]
    

    context = {
        'dates': dates,
        'steps': steps,
        'cardio_time': cardio_time,
        'cool_down_time': cool_down_time,
    }

    return render(request, 'fitness/report_chart.html', context)
