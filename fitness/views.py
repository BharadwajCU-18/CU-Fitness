# from django.shortcuts import render
# from .forms import FitnessForm
# from .models import FitnessReport

# def fitness_dashboard(request):
#     if request.method == 'POST':
#         form = FitnessForm(request.POST)
#         if form.is_valid():
#             report = form.save()  # Save the form data to the database
#             calories_burned = report.calculate_calories_burned()  # Calculate total calories burned
#             return render(request, 'fitness/report.html', {'form': form, 'calories_burned': calories_burned})
#     else:
#         form = FitnessForm()

#     return render(request, 'fitness/dashboard.html', {'form': form})


from django.shortcuts import render
from .forms import FitnessForm
from .models import FitnessReport

def fitness_dashboard(request):
    if request.method == 'POST':
        form = FitnessForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            report = form.save()

            # Ensure the calculate_calories_burned method exists in the FitnessReport model
            calories_burned = report.calculate_calories_burned()  

            # Render the 'report' template with form and calories burned info
            return render(request, 'fitness/report.html', {'form': form, 'calories_burned': calories_burned})
    else:
        form = FitnessForm()

    # If GET request or form not valid, render the dashboard template with the form
    return render(request, 'fitness/dashboard.html', {'form': form})

