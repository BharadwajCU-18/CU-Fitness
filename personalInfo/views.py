# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import UserPreferencesForm
# from .models import UserPreferences, Workout, Meal, Feedback

# # View for setting user preferences
# @login_required
# def set_user_preferences(request):
#     user_preferences = UserPreferences.objects.filter(user=request.user).first()

#     if request.method == "POST":
#         form = UserPreferencesForm(request.POST, instance=user_preferences)
#         if form.is_valid():
#             # Ensure that the user field is set correctly
#             user_preferences = form.save(commit=False)
#             user_preferences.user = request.user  # Set the user explicitly
#             user_preferences.save()
#             return redirect('preferences_success')  # Redirect to success page
#     else:
#         form = UserPreferencesForm(instance=user_preferences)

#     return render(request, 'chatbot/set_preferences.html', {'form': form})

# # View for personalized suggestions based on user preferences
# @login_required
# def get_personalized_suggestions(request):
#     try:
#         user_preferences = UserPreferences.objects.get(user=request.user)
#     except UserPreferences.DoesNotExist:
#         return redirect('set_user_preferences')  # Redirect to set preferences if none exist

#     # Filter workouts based on user preferences
#     workouts = Workout.objects.filter(category=user_preferences.preferred_workout_type)
#     print("Filtered Workouts:", workouts)  # Debug print statement

#     # Filter meals based on user preferences and dietary restrictions
#     meals = Meal.objects.filter(category=user_preferences.preferred_meal_type)
#     if user_preferences.dietary_restrictions:
#         meals = meals.filter(ingredients__contains=user_preferences.dietary_restrictions)
#     print("Filtered Meals:", meals)  # Debug print statement

#     return render(request, 'chatbot/personalized_suggestions.html', {'workouts': workouts, 'meals': meals})

# # View for submitting feedback
# @login_required
# def submit_feedback(request, item_type, item_id):
#     if request.method == 'POST':
#         rating = request.POST['rating']
#         comments = request.POST['comments']
        
#         # Determine the item being rated
#         if item_type == 'workout':
#             item = Workout.objects.get(id=item_id)
#         elif item_type == 'meal':
#             item = Meal.objects.get(id=item_id)
#         else:
#             return redirect('error_page')  # Redirect to error page if an invalid item type is provided

#         # Create feedback for the item
#         Feedback.objects.create(user=request.user, rating=rating, comments=comments, **{item_type: item})

#         return redirect('feedback_success')  # Redirect to success page

#     return render(request, 'chatbot/feedback_form.html', {'item_type': item_type, 'item_id': item_id})

# # View for a success message after submitting feedback
# def feedback_success(request):
#     return render(request, 'chatbot/feedback_success.html')

# # View for success after setting user preferences
# def preferences_success(request):
#     return render(request, 'chatbot/success.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserPreferencesForm
from .models import UserPreferences, Workout, Meal, Feedback
from django.http import JsonResponse
import openai
import logging

# Set up logger
logger = logging.getLogger(__name__)

# Set your OpenAI API key here
openai.api_key = 'api-key'  # Replace with your actual OpenAI API key
# View to render chatbot.html (home page)
def chatbot_home(request):
    return render(request, 'chatbot/chatbot.html')

# View to handle the chatbot response (API for processing user input)
def chatbot_response(request):
    if request.method == "GET":
        user_message = request.GET.get("message", "").strip()

        # Validate message
        if not user_message:
            return JsonResponse({"error": "Please enter a valid message."})

        try:
            # Call OpenAI API to get a response using the correct endpoint for chat models
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the chat-based model
                messages=[
                    {"role": "user", "content": user_message}
                ],
                max_tokens=150,
                temperature=0.7,
            )

            # Extract the bot's response
            bot_response = response['choices'][0]['message']['content'].strip()

            return JsonResponse({"response": bot_response})

        except openai.error.OpenAIError as e:
            return JsonResponse({"error": f"OpenAI error occurred: {str(e)} Please try again later."})

        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred. Please try again later."})

    return JsonResponse({"error": "Invalid request method."})

# View for setting user preferences
@login_required
def set_user_preferences(request):
    try:
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        user_preferences = None  # No preferences set yet, create new preferences for the user

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
    if not workouts.exists():
        workouts = None  # If no workouts match, return None

    # Filter meals based on user preferences and dietary restrictions
    meals = Meal.objects.filter(category=user_preferences.preferred_meal_type)
    if user_preferences.dietary_restrictions:
        meals = meals.filter(ingredients__contains=user_preferences.dietary_restrictions)
    print("Filtered Meals:", meals)  # Debug print statement
    
    if not meals.exists():
        meals = None  # If no meals match, return None

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
            try:
                item = Workout.objects.get(id=item_id)
            except Workout.DoesNotExist:
                return redirect('error_page')  # Redirect to error page if item does not exist
        elif item_type == 'meal':
            try:
                item = Meal.objects.get(id=item_id)
            except Meal.DoesNotExist:
                return redirect('error_page')  # Redirect to error page if item does not exist
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
