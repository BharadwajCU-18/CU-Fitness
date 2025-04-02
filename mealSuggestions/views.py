import random
import openai
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .forms import MealPreferencesForm
from .models import Meal, FavoriteMeal, RecommendationFeedback

@login_required
def submit_meal_preferences(request):
    meals = None  
    recommended_meals = []  # List to store ChatGPT's recommended meals
    search_done = False

    # Retrieve the user's favorite meals (only for authenticated users)
    favorite_meals = FavoriteMeal.objects.filter(user=request.user)

    if request.method == "POST" and "submit_preferences" in request.POST:
        search_done = True
        form = MealPreferencesForm(request.POST)
        
        if form.is_valid():
            dietary_restrictions = form.cleaned_data['dietary_restrictions']
            fitness_goals = form.cleaned_data['fitness_goals']
            meal_preferences = form.cleaned_data['meal_preferences']
            time_availability = form.cleaned_data['time_availability']
            budget = form.cleaned_data['budget']

            # Filter meals based on user preferences
            meal_queryset = Meal.objects.filter(
                dietary_restrictions=dietary_restrictions,
                fitness_goals=fitness_goals,
                meal_type=meal_preferences,
            )

            # Randomly select up to 3 meals from the matching meals
            if meal_queryset.exists():
                meals = random.sample(list(meal_queryset), min(3, meal_queryset.count()))
            else:
                meals = None

            # Generate ChatGPT prompt to recommend meals based on selected meals
            if meals:
                prompt = "Here are some meals you can choose from:\n\n"
                for meal in meals:
                    prompt += f"- {meal.name} (Diet: {meal.dietary_restrictions}): {meal.description}\n"

                prompt += "\nPlease suggest up to 3 of these meals based on your preferences."
                
                # Fetch user feedback (if available) to improve recommendations
                feedback_entries = RecommendationFeedback.objects.all()
                if feedback_entries.exists():
                    avg_rating = feedback_entries.aggregate(Avg('rating'))['rating__avg']
                    comments_list = [fb.comments for fb in feedback_entries if fb.comments]
                    feedback_text = f"User feedback average rating: {avg_rating:.1f}."
                    if comments_list:
                        feedback_text += " Comments: " + "; ".join(comments_list)
                    prompt += "\n" + feedback_text

                # Request ChatGPT for meal recommendations
                openai.api_key = settings.OPENAI_API_KEY
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "system", "content": "You are a meal recommendation assistant."},
                                  {"role": "user", "content": prompt}],
                        max_tokens=100,
                        temperature=0.5,  # Lower temperature for more deterministic results
                    )
                    chat_response = response.choices[0].message['content'].strip()
                    recommended_meals = [name.strip() for name in chat_response.split(",") if name.strip()]
                except Exception as e:
                    recommended_meals = []  # In case of error, set to an empty list

    else:
        form = MealPreferencesForm()

    # Pass all relevant data to the template
    return render(request, 'mealSuggestionsPage.html', {
        'form': form,
        'meals': meals,
        'recommended_meals': recommended_meals,
        'favorite_meals': favorite_meals,
        'search_done': search_done,
    })

@login_required
def add_to_favorites(request, meal_id):
    # Add the selected meal to the user's favorites
    meal = get_object_or_404(Meal, id=meal_id)
    FavoriteMeal.objects.get_or_create(user=request.user, meal=meal)
    return redirect('submit_meal_preferences')  # Redirect back to the preferences page

@login_required
def delete_favorite(request, favorite_id):
    # Remove the selected meal from the user's favorites
    favorite = get_object_or_404(FavoriteMeal, id=favorite_id, user=request.user)
    if request.method == 'POST':
        favorite.delete()
    return redirect('submit_meal_preferences')  # Redirect back to the preferences page

@login_required
def submit_feedback(request):
    """
    Handle feedback submission for each recommended meal.
    Expects multiple sets of data: meal_name_i, rating_i, comments_i.
    """
    if request.method == "POST":
        meal_count = int(request.POST.get("meal_count", "0"))
        for i in range(1, meal_count + 1):
            meal_name = request.POST.get(f"meal_name_{i}")
            rating = request.POST.get(f"rating_{i}")
            comments = request.POST.get(f"comments_{i}", "")
            if meal_name and rating:
                # Save the feedback data
                RecommendationFeedback.objects.create(
                    user=request.user,
                    meal_name=meal_name,
                    rating=rating,
                    comments=comments
                )
        return redirect('submit_meal_preferences')  # Redirect to preferences page after submitting feedback
