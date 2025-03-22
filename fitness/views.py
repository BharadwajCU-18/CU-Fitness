from django.shortcuts import render
from .forms import FitnessForm
from .models import FitnessReport

def fitness_dashboard(request):
    if request.method == 'POST':
        form = FitnessForm(request.POST)
        if form.is_valid():

            report = form.save()

            
            calories_burned = report.calculate_calories_burned()  

           
            return render(request, 'fitness/report.html', {'form': form, 'calories_burned': calories_burned})
    else:
        form = FitnessForm()

    
    return render(request, 'fitness/dashboard.html', {'form': form})

