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

    for entry in entries:
        date_str = entry.date.strftime('%Y-%m-%d')
        report[entry.date].append(entry)

        if date_str not in chart_labels:
            chart_labels.append(date_str)

        exercise_label = f"{entry.exercise_name}"

        if exercise_label not in datasets:
            datasets[exercise_label] = [0] * len(chart_labels)

        # Extend existing datasets if new date was added
        for label in datasets:
            while len(datasets[label]) < len(chart_labels):
                datasets[label].append(0)

        index = chart_labels.index(date_str)
        datasets[exercise_label][index] += entry.sets * entry.reps

    context = {
        'report': dict(report),
        'chart_labels': chart_labels,
        'datasets': datasets,
        'selected_month': month,
        'selected_year': year,
        'month_list': list(range(1, 13)),
        'year_list': list(range(2023, 2026)),
        'start_date': start_date.date(),
        'end_date': end_date.date(),
    }

    return render(request, 'fitnessReport.html', context)
