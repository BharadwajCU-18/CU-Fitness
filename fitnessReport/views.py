# # from datetime import datetime, timedelta
# # from collections import defaultdict
# # from django.shortcuts import render
# # from django.contrib.auth.decorators import login_required
# # from fitnessProgress.models import WorkoutEntry

# # @login_required
# # def fitness_report(request):
# #     today = datetime.today()
# #     month = int(request.GET.get('month', today.month))
# #     year = int(request.GET.get('year', today.year))

# #     start_date = datetime(year, month, 1)
# #     end_date = datetime(year + (month // 12), (month % 12) + 1, 1) - timedelta(days=1)

# #     entries = WorkoutEntry.objects.filter(user=request.user, date__range=[start_date, end_date])
# #     report = defaultdict(list)
# #     chart_labels = []
# #     datasets = {}

# #     for entry in entries:
# #         date_str = entry.date.strftime('%Y-%m-%d')
# #         report[entry.date].append(entry)

# #         if date_str not in chart_labels:
# #             chart_labels.append(date_str)

# #         exercise_label = f"{entry.exercise_name}"

# #         if exercise_label not in datasets:
# #             datasets[exercise_label] = [0] * len(chart_labels)

# #         # Extend existing datasets if new date was added
# #         for label in datasets:
# #             while len(datasets[label]) < len(chart_labels):
# #                 datasets[label].append(0)

# #         index = chart_labels.index(date_str)
# #         datasets[exercise_label][index] += entry.sets * entry.reps

# #     context = {
# #         'report': dict(report),
# #         'chart_labels': chart_labels,
# #         'datasets': datasets,
# #         'selected_month': month,
# #         'selected_year': year,
# #         'month_list': list(range(1, 13)),
# #         'year_list': list(range(2023, 2026)),
# #         'start_date': start_date.date(),
# #         'end_date': end_date.date(),
# #     }

# #     return render(request, 'fitnessReport.html', context)


# # from datetime import datetime, timedelta
# # from collections import defaultdict
# # from django.shortcuts import render
# # from django.contrib.auth.decorators import login_required
# # from fitnessProgress.models import WorkoutEntry

# # @login_required
# # def fitness_report(request):
# #     today = datetime.today()
# #     month = int(request.GET.get('month', today.month))
# #     year = int(request.GET.get('year', today.year))

# #     start_date = datetime(year, month, 1)
# #     end_date = datetime(year + (month // 12), (month % 12) + 1, 1) - timedelta(days=1)

# #     entries = WorkoutEntry.objects.filter(user=request.user, date__range=[start_date, end_date])
# #     report = defaultdict(list)
# #     chart_labels = []
# #     datasets = {}
# #     calories_per_day = defaultdict(int)  # New dictionary for calories

# #     for entry in entries:
# #         date_str = entry.date.strftime('%Y-%m-%d')
# #         report[entry.date].append(entry)

# #         if date_str not in chart_labels:
# #             chart_labels.append(date_str)

# #         # Track exercise dataset
# #         exercise_label = f"{entry.exercise_name}"

# #         if exercise_label not in datasets:
# #             datasets[exercise_label] = [0] * len(chart_labels)

# #         # Extend all datasets if a new date was added
# #         for label in datasets:
# #             while len(datasets[label]) < len(chart_labels):
# #                 datasets[label].append(0)

# #         index = chart_labels.index(date_str)
# #         datasets[exercise_label][index] += entry.sets * entry.reps

# #         # Track calories
# #         calories_per_day[date_str] += entry.calories_burned

# #     # Create calories dataset
# #     calories_data = [calories_per_day.get(date, 0) for date in chart_labels]
# #     datasets['Calories Burned'] = calories_data

# #     context = {
# #         'report': dict(report),
# #         'chart_labels': chart_labels,
# #         'datasets': datasets,
# #         'selected_month': month,
# #         'selected_year': year,
# #         'month_list': list(range(1, 13)),
# #         'year_list': list(range(2023, 2026)),
# #         'start_date': start_date.date(),
# #         'end_date': end_date.date(),
# #     }

# #     return render(request, 'fitnessReport.html', context)


# # from datetime import datetime, timedelta
# # from collections import defaultdict
# # from django.shortcuts import render
# # from django.contrib.auth.decorators import login_required
# # from fitnessProgress.models import WorkoutEntry

# # @login_required
# # def fitness_report(request):
# #     today = datetime.today()
# #     month = int(request.GET.get('month', today.month))
# #     year = int(request.GET.get('year', today.year))

# #     start_date = datetime(year, month, 1)
# #     end_date = datetime(year + (month // 12), (month % 12) + 1, 1) - timedelta(days=1)

# #     entries = WorkoutEntry.objects.filter(user=request.user, date__range=[start_date, end_date])
# #     report = defaultdict(list)
# #     chart_labels = []
# #     exercise_datasets = {}
# #     calories_data = []

# #     label_index_map = {}  # To keep consistent indexes

# #     for entry in entries:
# #         date_str = entry.date.strftime('%Y-%m-%d')
# #         report[entry.date].append(entry)

# #         if date_str not in chart_labels:
# #             chart_labels.append(date_str)
# #             label_index_map[date_str] = len(chart_labels) - 1
# #             calories_data.append(0)

# #         # Add exercise data
# #         exercise_label = entry.exercise_name
# #         if exercise_label not in exercise_datasets:
# #             exercise_datasets[exercise_label] = [0] * len(chart_labels)

# #         index = label_index_map[date_str]
# #         exercise_datasets[exercise_label][index] += entry.sets * entry.reps

# #         # Add calories burned
# #         calories_data[index] += getattr(entry, 'calories_burned', 0)

# #     context = {
# #         'report': dict(report),
# #         'chart_labels': chart_labels,
# #         'exercise_datasets': exercise_datasets,
# #         'calories_data': calories_data,
# #         'selected_month': month,
# #         'selected_year': year,
# #         'month_list': list(range(1, 13)),
# #         'year_list': list(range(2023, 2026)),
# #         'start_date': start_date.date(),
# #         'end_date': end_date.date(),
# #     }

# #     return render(request, 'fitnessReport.html', context)

# from datetime import datetime, timedelta
# from collections import defaultdict
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from fitnessProgress.models import WorkoutEntry

# @login_required
# def fitness_report(request):
#     today = datetime.today()
#     month = int(request.GET.get('month', today.month))
#     year = int(request.GET.get('year', today.year))

#     start_date = datetime(year, month, 1)
#     end_date = datetime(year + (month // 12), (month % 12) + 1, 1) - timedelta(days=1)

#     entries = WorkoutEntry.objects.filter(user=request.user, date__range=[start_date, end_date])
#     report = defaultdict(list)
#     chart_labels = []
#     exercise_datasets = {}
#     calories_data = []

#     label_index_map = {}  # To keep consistent indexes

#     # Prepare data for both graphs
#     for entry in entries:
#         date_str = entry.date.strftime('%Y-%m-%d')
#         report[entry.date].append(entry)

#         if date_str not in chart_labels:
#             chart_labels.append(date_str)
#             label_index_map[date_str] = len(chart_labels) - 1
#             calories_data.append(0)

#         # Exercise data (for reps graph)
#         exercise_label = entry.exercise_name
#         if exercise_label not in exercise_datasets:
#             exercise_datasets[exercise_label] = [0] * len(chart_labels)

#         index = label_index_map[date_str]
#         exercise_datasets[exercise_label][index] += entry.sets * entry.reps

#         # Add calories burned to the calories_data list
#         calories_data[index] += getattr(entry, 'calories_burned', 0)

#     context = {
#         'report': dict(report),
#         'chart_labels': chart_labels,
#         'exercise_datasets': exercise_datasets,
#         'calories_data': calories_data,
#         'selected_month': month,
#         'selected_year': year,
#         'month_list': list(range(1, 13)),
#         'year_list': list(range(2023, 2026)),
#         'start_date': start_date.date(),
#         'end_date': end_date.date(),
#     }

#     return render(request, 'fitnessReport.html', context)
# from datetime import datetime, timedelta
# from collections import defaultdict
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from fitnessProgress.models import WorkoutEntry

# @login_required
# def fitness_report(request):
#     today = datetime.today()
#     month = int(request.GET.get('month', today.month))
#     year = int(request.GET.get('year', today.year))

#     start_date = datetime(year, month, 1)
#     end_date = datetime(year + (month // 12), (month % 12) + 1, 1) - timedelta(days=1)

#     entries = WorkoutEntry.objects.filter(user=request.user, date__range=[start_date, end_date])
#     report = defaultdict(list)
#     chart_labels = []
#     exercise_datasets = {}
#     calories_data = []

#     label_index_map = {}  # To keep consistent indexes

#     # Prepare data for both graphs
#     for entry in entries:
#         date_str = entry.date.strftime('%Y-%m-%d')
#         report[entry.date].append(entry)

#         # Ensure chart_labels and label_index_map are synced
#         if date_str not in label_index_map:
#             chart_labels.append(date_str)
#             label_index_map[date_str] = len(chart_labels) - 1
#             calories_data.append(0)  # Add placeholder for calories

#             # Extend all exercise datasets to include space for the new date
#             for exercise_label in exercise_datasets:
#                 exercise_datasets[exercise_label].append(0)

#         # Get the index of the current date_str in chart_labels
#         index = label_index_map[date_str]

#         # Exercise data (for reps graph)
#         exercise_label = entry.exercise_name
#         if exercise_label not in exercise_datasets:
#             # Ensure the dataset for this exercise is created with zeros for all existing labels
#             exercise_datasets[exercise_label] = [0] * len(chart_labels)

#         # Add sets * reps to the appropriate index for the exercise
#         exercise_datasets[exercise_label][index] += entry.sets * entry.reps

#         # Add calories burned to the calories_data list
#         calories_data[index] += getattr(entry, 'calories_burned', 0)

#     # Debugging: Print out chart labels and their corresponding data
#     print(f"Chart Labels: {chart_labels}")
#     print(f"Exercise Datasets: {exercise_datasets}")
#     print(f"Calories Data: {calories_data}")

#     # Ensure the lengths match before rendering
#     assert len(chart_labels) == len(calories_data), f"Mismatch between chart_labels and calories_data lengths. {len(chart_labels)} vs {len(calories_data)}"
#     for label, dataset in exercise_datasets.items():
#         assert len(dataset) == len(chart_labels), f"Mismatch in length of dataset for {label}. {len(dataset)} vs {len(chart_labels)}"

#     context = {
#         'report': dict(report),
#         'chart_labels': chart_labels,
#         'exercise_datasets': exercise_datasets,
#         'calories_data': calories_data,
#         'selected_month': month,
#         'selected_year': year,
#         'month_list': list(range(1, 13)),
#         'year_list': list(range(2023, 2026)),
#         'start_date': start_date.date(),
#         'end_date': end_date.date(),
#     }

#     return render(request, 'fitnessReport.html', context)



# Add this to your imports at the top


from datetime import datetime, timedelta
from collections import defaultdict
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fitnessProgress.models import WorkoutEntry

@login_required
def fitness_report(request):
    today = datetime.today()
    
    month = int(request.GET.get('month', today.month))
    year = int(request.GET.get('year', today.year))
    
    start_date = datetime(year, month, 1)
    end_date = datetime(year + (month // 12), (month % 12) + 1, 1) - timedelta(days=1)
    
    entries = WorkoutEntry.objects.filter(user=request.user, date__range=[start_date, end_date])
    
    report = defaultdict(list)
    chart_labels = []
    datasets = {}
    calories_data = {}
    
    for entry in entries:
        date_str = entry.date.strftime('%Y-%m-%d')
        report[entry.date].append(entry)

        if date_str not in chart_labels:
            chart_labels.append(date_str)

        exercise_label = f"{entry.exercise_name}"
        calories = entry.sets * entry.reps * 0.3  # Updated multiplier for calories burned

        if exercise_label not in datasets:
            datasets[exercise_label] = [0] * len(chart_labels)

        for label in datasets:
            while len(datasets[label]) < len(chart_labels):
                datasets[label].append(0)

        index = chart_labels.index(date_str)
        datasets[exercise_label][index] += entry.sets * entry.reps
        calories_data[date_str] = calories_data.get(date_str, 0) + calories

    # Prepare the calories dataset
    calories_dataset = [calories_data.get(label, 0) for label in chart_labels]

    context = {
        'report': dict(report),
        'chart_labels': chart_labels,
        'datasets': datasets,
        'calories_dataset': calories_dataset,
        'selected_month': month,
        'selected_year': year,
        'month_list': list(range(1, 13)),
        'year_list': list(range(2023, 2026)),
        'start_date': start_date.date(),
        'end_date': end_date.date(),
    }
    
    return render(request, 'fitnessReport.html', context)
