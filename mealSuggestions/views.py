# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import MealPreferencesForm
# from .models import Meal, FavoriteMeal
# from django.template import loader
# import random
# from django.http import HttpResponse

# # @login_required
# def submit_meal_preferences(request):
#     meals = None  
#     favorite_meals = FavoriteMeal.objects.filter(user=request.user)  # Fetch user's favorite meals

#     if request.method == "POST" and "submit_preferences" in request.POST:
#         form = MealPreferencesForm(request.POST)
#         if form.is_valid():
#             dietary_restrictions = form.cleaned_data['dietary_restrictions']
#             fitness_goals = form.cleaned_data['fitness_goals']
#             meal_preferences = form.cleaned_data['meal_preferences']
#             time_availability = form.cleaned_data['time_availability']
#             budget = form.cleaned_data['budget']

#             # Filter meals based on user preferences
#             meals = Meal.objects.filter(
#                 dietary_restrictions=dietary_restrictions,
#                 fitness_goals=fitness_goals,
#                 meal_type=meal_preferences,
#                 time_required__lte=int(time_availability.split('_')[0]),
#                 budget__lte=budget
#             )

#             # Select up to 3 random meals
#             meals = random.sample(list(meals), min(3, len(meals))) if meals.exists() else None

#     else:
#         form = MealPreferencesForm()

#     return render(request, 'mealSuggestionsPage.html', {
#         'form': form,
#         'meals': meals,
#         'favorite_meals': favorite_meals
#     })
#     # template = loader.get_template('mealSuggestionsPage.html')
#     # return HttpResponse(template.render())
# # @login_required
# def add_to_favorites(request, meal_id):
#     meal = get_object_or_404(Meal, id=meal_id)
#     FavoriteMeal.objects.get_or_create(user=request.user, meal=meal)  # Prevent duplicates
#     return redirect('submit_meal_preferences')  # Reload page to reflect favorite meals
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required  # Login decorator commented out
from .forms import MealPreferencesForm
from .models import Meal, FavoriteMeal
import random

# @login_required  # Commented out login requirement
def submit_meal_preferences(request):
    meals = None  
    # Use authenticated user's favorites; if not authenticated, default to an empty list.
    if request.user.is_authenticated:
        favorite_meals = FavoriteMeal.objects.filter(user=request.user)
    else:
        favorite_meals = []

    if request.method == "POST" and "submit_preferences" in request.POST:
        form = MealPreferencesForm(request.POST)
        if form.is_valid():
            dietary_restrictions = form.cleaned_data['dietary_restrictions']
            fitness_goals = form.cleaned_data['fitness_goals']
            meal_preferences = form.cleaned_data['meal_preferences']
            time_availability = form.cleaned_data['time_availability']
            budget = form.cleaned_data['budget']

            # Filter meals based on user preferences
            meals_queryset = Meal.objects.filter(
                dietary_restrictions=dietary_restrictions,
                fitness_goals=fitness_goals,
                meal_type=meal_preferences,
                # time_required__lte=int(time_availability.split('_')[0]),
                # budget__lte=budget
            )

            # Select up to 3 random meals if available
            if meals_queryset.exists():
                meals = random.sample(list(meals_queryset), min(3, meals_queryset.count()))
            else:
                meals = None
    else:
        form = MealPreferencesForm()

    return render(request, 'mealSuggestionsPage.html', {
        'form': form,
        'meals': meals,
        'favorite_meals': favorite_meals
    })

# @login_required  # Commented out login requirement
def add_to_favorites(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    # Only add to favorites if the user is authenticated
    if request.user.is_authenticated:
        FavoriteMeal.objects.get_or_create(user=request.user, meal=meal)
    # If the user is not authenticated, you might want to handle it differently
    return redirect('submit_meal_preferences')
