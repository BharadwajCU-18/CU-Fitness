# from django.shortcuts import render, redirect
# from .forms import FitnessProgressForm

# from .models import FitnessReport

# def fitness_dashboard(request):
#     if request.method == 'POST':
#         form = FitnessProgressForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return redirect('fitness_dashboard')  # Redirect back to the form page
#     else:
#         form = FitnessProgressForm()

#     return render(request, 'fitness/dashboard.html', {'form': form})


# # views.py


# def fitness_report_chart(request):
#     # Get the data from the database
#     fitness_reports = FitnessReport.objects.all()
#     dates = [report.date.strftime('%Y-%m-%d') for report in fitness_reports]
#     steps = [report.steps for report in fitness_reports]
#     cardio_time = [report.cardio_time for report in fitness_reports]
#     cool_down_time = [report.cool_down_time for report in fitness_reports]
    

#     context = {
#         'dates': dates,
#         'steps': steps,
#         'cardio_time': cardio_time,
#         'cool_down_time': cool_down_time,
#     }

#     return render(request, 'fitness/report_chart.html', context)



# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import FitnessProgressForm
# from .models import FitnessReport

# @login_required
# def fitness_dashboard(request):
#     if request.method == 'POST':
#         form = FitnessProgressForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.user = request.user  # Save the logged-in user
#             report.save()
#             return redirect('fitness_dashboard')  
#     else:
#         form = FitnessProgressForm()

#     return render(request, 'fitness/dashboard.html', {'form': form})


# @login_required
# def fitness_report_chart(request):
#     # Filter reports for the logged-in user
#     fitness_reports = FitnessReport.objects.filter(user=request.user).order_by('date')

#     dates = [report.date.strftime('%Y-%m-%d') for report in fitness_reports]
#     steps = [report.steps for report in fitness_reports]
#     cardio_time = [report.cardio_time for report in fitness_reports]
#     cool_down_time = [report.cool_down_time for report in fitness_reports]

#     context = {
#         'dates': dates,
#         'steps': steps,
#         'cardio_time': cardio_time,
#         'cool_down_time': cool_down_time,
#     }

#     return render(request, 'fitness/report_chart.html', context)


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import FitnessProgressForm
# from .models import FitnessReport

# @login_required
# def fitness_dashboard(request):
#     if request.method == 'POST':
#         form = FitnessProgressForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.user = request.user  # Automatically associate with the logged-in user
#             report.save()
#             return redirect('fitness_dashboard')  # Redirect after saving
#     else:
#         form = FitnessProgressForm()

#     return render(request, 'fitness/dashboard.html', {'form': form})

# @login_required
# def fitness_report_chart(request):
#     # Filter reports for the logged-in user
#     fitness_reports = FitnessReport.objects.filter(user=request.user).order_by('date')

#     dates = [report.date.strftime('%Y-%m-%d') for report in fitness_reports]
#     steps = [report.steps for report in fitness_reports]
#     cardio_time = [report.cardio_time for report in fitness_reports]
#     cool_down_time = [report.cool_down_time for report in fitness_reports]

#     context = {
#         'dates': dates,
#         'steps': steps,
#         'cardio_time': cardio_time,
#         'cool_down_time': cool_down_time,
#     }

#     return render(request, 'fitness/report_chart.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FitnessProgressForm
from .models import FitnessReport

@login_required
def fitness_dashboard(request):
    if request.method == 'POST':
        form = FitnessProgressForm(request.POST)
        if form.is_valid():
            # Form is valid, we save it
            report = form.save(commit=False)  # Create the instance without saving to DB yet
            report.user = request.user  # Assign the logged-in user to the report
            report.save()  # Save the report to the database
            return redirect('fitness_dashboard')  # Redirect to the same page after saving
        else:
            # Print form errors for debugging
            print(form.errors)  # This will show any validation issues in the console
    else:
        form = FitnessProgressForm()  # Empty form when GET request

    return render(request, 'fitness/dashboard.html', {'form': form})


@login_required
def fitness_report_chart(request):
    # Filter reports for the logged-in user
    fitness_reports = FitnessReport.objects.filter(user=request.user).order_by('date')

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