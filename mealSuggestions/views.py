import random
import openai
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .forms import MealPreferencesForm, RecommendationFeedbackForm
from .models import Meal, FavoriteMeal, RecommendationFeedback

@login_required
def submit_meal_preferences(request):
    meals = None  
    recommended_meals = []  # Will store the names of recommended meals from ChatGPT  need to remove this
    favorite_meals = FavoriteMeal.objects.filter(user=request.user)
    search_done = False

    if request.method == "POST" and "submit_preferences" in request.POST:
        search_done = True
        form = MealPreferencesForm(request.POST)
        if form.is_valid():
            dietary_restrictions = form.cleaned_data['dietary_restrictions']
            fitness_goals = form.cleaned_data['fitness_goals']
            meal_preferences = form.cleaned_data['meal_preferences']

            # Retrieve all matching meals from the database
            meal_queryset = Meal.objects.filter(
                dietary_restrictions=dietary_restrictions,
                fitness_goals=fitness_goals,
                meal_type=meal_preferences,
            )
            meals_list = list(meal_queryset)

            if meals_list:
                # Randomly select up to 3 meals from the matching set for display
                display_meals = random.sample(meals_list, min(3, len(meals_list)))

                # Build a prompt that lists ONLY the selected meals so that ChatGPT
                # can only choose from these and not invent new meal names.
                prompt = "You are given the following meal options. Do NOT invent any new meal names. Only choose from the list below:\n\n"
                for meal in display_meals:
                    favorite_count = FavoriteMeal.objects.filter(meal=meal).count()
                    prompt += f"- {meal.name} (Diet: {meal.dietary_restrictions}, Favorites: {favorite_count}): {meal.description}\n"
                prompt += ("\nBased solely on these options, please recommend up to 3 meal names that best match the user's preferences. "
                           "Return the names as a comma-separated list with no additional text.")

                # (Optional) Append aggregated feedback from previous submissions
                feedback_entries = RecommendationFeedback.objects.all()
                if feedback_entries.exists():
                    avg_rating = feedback_entries.aggregate(Avg('rating'))['rating__avg']
                    comments_list = [fb.comments for fb in feedback_entries if fb.comments]
                    feedback_text = f" User feedback average rating: {avg_rating:.1f}."
                    if comments_list:
                        feedback_text += " Comments: " + "; ".join(comments_list)
                    prompt += "\n" + feedback_text

                # Call the OpenAI API to get recommendations
                openai.api_key = settings.OPENAI_API_KEY
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a meal recommendation assistant."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=100,
                        temperature=0.3,  # Lower temperature to follow the instructions strictly
                    )
                    chat_response = response.choices[0].message['content'].strip()
                    # Parse the comma-separated list
                    recommended_meals = [name.strip() for name in chat_response.split(",") if name.strip()]
                    # Filter: Only keep names that exist in the selected subset
                    valid_meal_names = [meal.name for meal in display_meals]
                    recommended_meals = [name for name in recommended_meals if name in valid_meal_names]
                except Exception as e:
                    recommended_meals = []

                meals = display_meals
            else:
                meals = None
    else:
        form = MealPreferencesForm()

    return render(request, 'mealSuggestionsPage.html', {
        'form': form,
        'meals': meals,
        'favorite_meals': favorite_meals,
        'recommended_meals': recommended_meals,
        'search_done': search_done,
    })

@login_required
def add_to_favorites(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    FavoriteMeal.objects.get_or_create(user=request.user, meal=meal)
    return redirect('submit_meal_preferences')

@login_required
def delete_favorite(request, favorite_id):
    favorite = get_object_or_404(FavoriteMeal, id=favorite_id, user=request.user)
    if request.method == 'POST':
        favorite.delete()
    return redirect('submit_meal_preferences')

@login_required
def submit_feedback(request):
    """
    Process feedback for each recommended meal.
    Expects multiple sets of data: meal_name_i, rating_i, comments_i.
    """
    if request.method == "POST":
        meal_count = int(request.POST.get("meal_count", "0"))
        for i in range(1, meal_count + 1):
            meal_name = request.POST.get(f"meal_name_{i}")
            rating = request.POST.get(f"rating_{i}")
            comments = request.POST.get(f"comments_{i}", "")
            if meal_name and rating:
                RecommendationFeedback.objects.create(
                    user=request.user,
                    meal_name=meal_name,
                    rating=rating,
                    comments=comments
                )
    return redirect('submit_meal_preferences')
