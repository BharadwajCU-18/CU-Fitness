from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserPreferencesForm
from .models import UserPreferences, Workout, Meal, Feedback
from django.http import JsonResponse
from django.conf import settings
import openai
import logging

# Set up logger
logger = logging.getLogger(__name__)
import os

openai.api_key = settings.OPENAI_API_KEY
# Home page view
def chatbot_home(request):
    return render(request, 'chatbot/chatbot.html')



# Chatbot response view with personalization
def chatbot_response(request):
    if request.method == "GET":
        user_message = request.GET.get("message", "").strip()

        if not user_message:
            return JsonResponse({"error": "Please enter a valid message."})

        try:
            # Initialize user_context
            user_context = ""

            # Add user preferences if authenticated
            if request.user.is_authenticated:
                try:
                    prefs = UserPreferences.objects.get(user=request.user)
                    user_context = (
                        f"The user prefers {prefs.preferred_workout_type} workouts and "
                        f"{prefs.preferred_meal_type} meals. Dietary restrictions include "
                        f"{prefs.dietary_restrictions or 'none'}."
                    )
                except UserPreferences.DoesNotExist:
                    user_context = "The user has not set any preferences."
            else:
                user_context = "The user is not logged in, so no preferences are available."

            # Call the OpenAI API with the personalized context
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a friendly and helpful fitness assistant."},
                    {"role": "system", "content": user_context},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=150,
                temperature=0.7,
            )

            bot_response = response['choices'][0]['message']['content'].strip()
            return JsonResponse({"response": bot_response})

        except openai.error.OpenAIError as e:
            return JsonResponse({"error": f"OpenAI error occurred: {str(e)} Please try again later."})
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred. Please try again later."})

    return JsonResponse({"error": "Invalid request method."})
# def chatbot_response(request):
#     if request.method == "GET":
#         user_message = request.GET.get("message", "").strip()

#         if not user_message:
#             return JsonResponse({"error": "Please enter a valid message."})

#         try:
#             user_context = ""

#             # Add user preferences if authenticated
#             if request.user.is_authenticated:
#                 try:
#                     prefs = UserPreferences.objects.get(user=request.user)
#                     user_context = (
#                         f"The user prefers {prefs.preferred_workout_type} workouts and "
#                         f"{prefs.preferred_meal_type} meals. Dietary restrictions include "
#                         f"{prefs.dietary_restrictions or 'none'}."
#                     )
#                 except UserPreferences.DoesNotExist:
#                     user_context = "The user has not set any preferences."
#             else:
#                 user_context = "The user is not logged in, so no preferences are available."

#             messages = [
#                 {"role": "system", "content": "You are a helpful fitness and nutrition assistant."},
#                 {"role": "system", "content": user_context},
#                 {"role": "user", "content": user_message},
#             ]

#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=messages,
#                 max_tokens=150,
#                 temperature=0.7,
#             )

#             bot_response = response['choices'][0]['message']['content'].strip()
#             return JsonResponse({"response": bot_response})

#         except openai.error.OpenAIError as e:
#             return JsonResponse({"error": f"OpenAI error occurred: {str(e)} Please try again later."})
#         except Exception as e:
#             logger.error(f"Unexpected error: {str(e)}")
#             return JsonResponse({"error": "An unexpected error occurred. Please try again later."})

#     return JsonResponse({"error": "Invalid request method."})

# Set user preferences
@login_required
def set_user_preferences(request):
    try:
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        user_preferences = None

    if request.method == "POST":
        form = UserPreferencesForm(request.POST, instance=user_preferences)
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.user = request.user
            preferences.save()
            return redirect('chatbot:preferences_success')
    else:
        form = UserPreferencesForm(instance=user_preferences)

    return render(request, 'chatbot/set_preferences.html', {'form': form})

# View for showing personalized workout/meal suggestions
@login_required
def get_personalized_suggestions(request):
    try:
        user_preferences = UserPreferences.objects.get(user=request.user)
    except UserPreferences.DoesNotExist:
        return redirect('chatbot:set_preferences')  # Redirect to the preferences page if not set

    # Fetch personalized workouts and meals based on user preferences
    workouts = Workout.objects.filter(category__iexact=user_preferences.preferred_workout_type)
    if not workouts.exists():
        workouts = Workout.objects.all()  # Fallback to all workouts if none match

    meals = Meal.objects.filter(category__iexact=user_preferences.preferred_meal_type)
    if user_preferences.dietary_restrictions:
        meals = meals.filter(ingredients__icontains=user_preferences.dietary_restrictions)
    if not meals.exists():
        meals = Meal.objects.all()  # Fallback to all meals if none match

    return render(request, 'chatbot/personalized_suggestions.html', {
        'workouts': workouts,
        'meals': meals,
        'preferences': user_preferences,
    })
# Submit feedback for a workout or meal
@login_required
def submit_feedback(request, item_type, item_id):
    if request.method == 'POST':
        rating = request.POST['rating']
        comments = request.POST['comments']

        if item_type == 'workout':
            try:
                item = Workout.objects.get(id=item_id)
            except Workout.DoesNotExist:
                logger.error(f"Workout with ID {item_id} does not exist.")
                return redirect('error_page')
        elif item_type == 'meal':
            try:
                item = Meal.objects.get(id=item_id)
            except Meal.DoesNotExist:
                logger.error(f"Meal with ID {item_id} does not exist.")
                return redirect('error_page')
        else:
            logger.error(f"Invalid item type: {item_type}")
            return redirect('error_page')

        Feedback.objects.create(user=request.user, rating=rating, comments=comments, **{item_type: item})
        return redirect('chatbot:feedback_success')

    return render(request, 'chatbot/feedback_form.html', {'item_type': item_type, 'item_id': item_id})

# Success page after submitting feedback
def feedback_success(request):
    return render(request, 'chatbot/feedback_success.html')

# Success page after setting preferences
def preferences_success(request):
    return render(request, 'chatbot/success.html')
