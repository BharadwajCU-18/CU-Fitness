from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserPreferencesForm
from .models import UserPreferences, Workout, Meal, Feedback

# View for setting user preferences
@login_required
def set_user_preferences(request):
    user_preferences = UserPreferences.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = UserPreferencesForm(request.POST, instance=user_preferences)
        if form.is_valid():
            # Ensure that the user field is set correctly
            user_preferences = form.save(commit=False)
            user_preferences.user = request.user  # Set the user explicitly
            user_preferences.save()
            return redirect('preferences_success')  # Redirect to success page
    else:
        form = UserPreferencesForm(instance=user_preferences)

    return render(request, 'chatbot/set_preferences.html', {'form': form})

# View for personalized suggestions based on user preferences
@login_required
def get_personalized_suggestions(request):
    try:
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        return redirect('set_user_preferences')  # Redirect to set preferences if none exist

    # Filter workouts based on user preferences
    workouts = Workout.objects.filter(category=user_preferences.preferred_workout_type)
    print("Filtered Workouts:", workouts)  # Debug print statement

    # Filter meals based on user preferences and dietary restrictions
    meals = Meal.objects.filter(category=user_preferences.preferred_meal_type)
    if user_preferences.dietary_restrictions:
        meals = meals.filter(ingredients__contains=user_preferences.dietary_restrictions)
    print("Filtered Meals:", meals)  # Debug print statement

    return render(request, 'chatbot/personalized_suggestions.html', {'workouts': workouts, 'meals': meals})

# View for submitting feedback
@login_required
def submit_feedback(request, item_type, item_id):
    if request.method == 'POST':
        rating = request.POST['rating']
        comments = request.POST['comments']
        
        # Determine the item being rated
        if item_type == 'workout':
            item = Workout.objects.get(id=item_id)
        elif item_type == 'meal':
            item = Meal.objects.get(id=item_id)
        else:
            return redirect('error_page')  # Redirect to error page if an invalid item type is provided

        # Create feedback for the item
        Feedback.objects.create(user=request.user, rating=rating, comments=comments, **{item_type: item})

        return redirect('feedback_success')  # Redirect to success page

    return render(request, 'chatbot/feedback_form.html', {'item_type': item_type, 'item_id': item_id})

# View for a success message after submitting feedback
def feedback_success(request):
    return render(request, 'chatbot/feedback_success.html')

# View for success after setting user preferences
def preferences_success(request):
    return render(request, 'chatbot/success.html')
