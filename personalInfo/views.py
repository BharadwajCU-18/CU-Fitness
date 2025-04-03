# # from django.shortcuts import render, redirect
# # from django.contrib.auth.decorators import login_required
# # from .forms import UserPreferencesForm
# # from .models import UserPreferences, Workout, Meal, Feedback

# # # View for setting user preferences
# # @login_required
# # def set_user_preferences(request):
# #     user_preferences = UserPreferences.objects.filter(user=request.user).first()

# #     if request.method == "POST":
# #         form = UserPreferencesForm(request.POST, instance=user_preferences)
# #         if form.is_valid():
# #             # Ensure that the user field is set correctly
# #             user_preferences = form.save(commit=False)
# #             user_preferences.user = request.user  # Set the user explicitly
# #             user_preferences.save()
# #             return redirect('preferences_success')  # Redirect to success page
# #     else:
# #         form = UserPreferencesForm(instance=user_preferences)

# #     return render(request, 'chatbot/set_preferences.html', {'form': form})

# # # View for personalized suggestions based on user preferences
# # @login_required
# # def get_personalized_suggestions(request):
# #     try:
# #         user_preferences = UserPreferences.objects.get(user=request.user)
# #     except UserPreferences.DoesNotExist:
# #         return redirect('set_user_preferences')  # Redirect to set preferences if none exist

# #     # Filter workouts based on user preferences
# #     workouts = Workout.objects.filter(category=user_preferences.preferred_workout_type)
# #     print("Filtered Workouts:", workouts)  # Debug print statement

# #     # Filter meals based on user preferences and dietary restrictions
# #     meals = Meal.objects.filter(category=user_preferences.preferred_meal_type)
# #     if user_preferences.dietary_restrictions:
# #         meals = meals.filter(ingredients__contains=user_preferences.dietary_restrictions)
# #     print("Filtered Meals:", meals)  # Debug print statement

# #     return render(request, 'chatbot/personalized_suggestions.html', {'workouts': workouts, 'meals': meals})

# # # View for submitting feedback
# # @login_required
# # def submit_feedback(request, item_type, item_id):
# #     if request.method == 'POST':
# #         rating = request.POST['rating']
# #         comments = request.POST['comments']
        
# #         # Determine the item being rated
# #         if item_type == 'workout':
# #             item = Workout.objects.get(id=item_id)
# #         elif item_type == 'meal':
# #             item = Meal.objects.get(id=item_id)
# #         else:
# #             return redirect('error_page')  # Redirect to error page if an invalid item type is provided

# #         # Create feedback for the item
# #         Feedback.objects.create(user=request.user, rating=rating, comments=comments, **{item_type: item})

# #         return redirect('feedback_success')  # Redirect to success page

# #     return render(request, 'chatbot/feedback_form.html', {'item_type': item_type, 'item_id': item_id})

# # # View for a success message after submitting feedback
# # def feedback_success(request):
# #     return render(request, 'chatbot/feedback_success.html')

# # # View for success after setting user preferences
# # def preferences_success(request):
# #     return render(request, 'chatbot/success.html')
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from chatbot.forms import UserPreferencesForm
# from chatbot.models import UserPreferences, Workout, Meal, Feedback
# from django.http import JsonResponse
# import openai
# import logging


# # Set up logger
# logger = logging.getLogger(__name__)

# # Set your OpenAI API key here
# openai.api_key = 'api-key'  # Replace with your actual OpenAI API key
# # View to render chatbot.html (home page)
# def chatbot_home(request):
#     return render(request, 'chatbot/chatbot.html')

# # View to handle the chatbot response (API for processing user input)
# def chatbot_response(request):
#     if request.method == "GET":
#         user_message = request.GET.get("message", "").strip()

#         # Validate message
#         if not user_message:
#             return JsonResponse({"error": "Please enter a valid message."})

#         try:
#             # Call OpenAI API to get a response using the correct endpoint for chat models
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",  # Use the chat-based model
#                 messages=[
#                     {"role": "user", "content": user_message}
#                 ],
#                 max_tokens=150,
#                 temperature=0.7,
#             )

#             # Extract the bot's response
#             bot_response = response['choices'][0]['message']['content'].strip()

#             return JsonResponse({"response": bot_response})

#         except openai.error.OpenAIError as e:
#             return JsonResponse({"error": f"OpenAI error occurred: {str(e)} Please try again later."})

#         except Exception as e:
#             return JsonResponse({"error": "An unexpected error occurred. Please try again later."})

#     return JsonResponse({"error": "Invalid request method."})

# # View for setting user preferences
# @login_required
# def set_user_preferences(request):
#     try:
#         user_preferences = UserPreferences.objects.get(user=request.user)
#     except UserPreferences.DoesNotExist:
#         user_preferences = None  # No preferences set yet, create new preferences for the user

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
#     if not workouts.exists():
#         workouts = None  # If no workouts match, return None

#     # Filter meals based on user preferences and dietary restrictions
#     meals = Meal.objects.filter(category=user_preferences.preferred_meal_type)
#     if user_preferences.dietary_restrictions:
#         meals = meals.filter(ingredients__contains=user_preferences.dietary_restrictions)
#     print("Filtered Meals:", meals)  # Debug print statement
    
#     if not meals.exists():
#         meals = None  # If no meals match, return None

#     return render(request, 'chatbot/personalized_suggestions.html', {'workouts': workouts, 'meals': meals})

# # View for submitting feedback
# @login_required
# # Corrected version of the submit_feedback function
# @login_required
# def submit_feedback(request, item_type, item_id):
#     if request.method == 'POST':
#         rating = request.POST['rating']
#         comments = request.POST['comments']
        
#         # Determine the item being rated
#         if item_type == 'workout':
#             try:
#                 item = Workout.objects.get(id=item_id)
#             except Workout.DoesNotExist:
#                 return redirect('error_page')  # Redirect to error page if item does not exist
#         elif item_type == 'meal':
#             try:
#                 item = Meal.objects.get(id=item_id)
#             except Meal.DoesNotExist:
#                 return redirect('error_page')  # Redirect to error page if item does not exist
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
from chatbot.forms import UserPreferencesForm
from chatbot.models import UserPreferences, Workout, Meal, Feedback
# from django.contrib.auth.forms import UserCreationForm
from personalInfo.forms import RegistrationForm, FitnessInformationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib import messages
import openai
import logging
import os

# Set up logger
logger = logging.getLogger(__name__)

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# # View to render chatbot home page
# def chatbot_home(request):
#     return render(request, 'chatbot/chatbot.html')

# # View to handle chatbot response
# def chatbot_response(request):
#     if request.method == "GET":
#         user_message = request.GET.get("message", "").strip()

#         # Validate message
#         if not user_message:
#             return JsonResponse({"error": "Please enter a valid message."})

#         try:
#             # Call OpenAI API to get a response
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": user_message}],
#                 max_tokens=150,
#                 temperature=0.7,
#             )

#             bot_response = response['choices'][0]['message']['content'].strip()
#             return JsonResponse({"response": bot_response})

#         except openai.error.OpenAIError as e:
#             return JsonResponse({"error": f"OpenAI error occurred: {str(e)} Please try again later."})

#         except Exception as e:
#             return JsonResponse({"error": "An unexpected error occurred. Please try again later."})

#     return JsonResponse({"error": "Invalid request method."})

# # View for setting user preferences
# @login_required
# def set_user_preferences(request):
#     user_preferences, created = UserPreferences.objects.get_or_create(user=request.user)

#     if request.method == "POST":
#         form = UserPreferencesForm(request.POST, instance=user_preferences)
#         if form.is_valid():
#             form.save()
#             return redirect('preferences_success')
#     else:
#         form = UserPreferencesForm(instance=user_preferences)

#     return render(request, 'chatbot/set_preferences.html', {'form': form})

# # View for personalized suggestions based on user preferences
# @login_required
# def get_personalized_suggestions(request):
#     try:
#         user_preferences = UserPreferences.objects.get(user=request.user)
#     except UserPreferences.DoesNotExist:
#         return redirect('set_user_preferences')

#     workouts = Workout.objects.filter(category=user_preferences.preferred_workout_type)
#     if not workouts.exists():
#         workouts = None

#     meals = Meal.objects.filter(category=user_preferences.preferred_meal_type)
#     if user_preferences.dietary_restrictions:
#         meals = meals.filter(ingredients__contains=user_preferences.dietary_restrictions)
#     if not meals.exists():
#         meals = None

#     return render(request, 'chatbot/personalized_suggestions.html', {'workouts': workouts, 'meals': meals})

# # View for submitting feedback
# @login_required
# def submit_feedback(request, item_type, item_id):
#     if request.method == 'POST':
#         rating = request.POST['rating']
#         comments = request.POST['comments']

#         if item_type == 'workout':
#             try:
#                 item = Workout.objects.get(id=item_id)
#             except Workout.DoesNotExist:
#                 return redirect('error_page')
#         elif item_type == 'meal':
#             try:
#                 item = Meal.objects.get(id=item_id)
#             except Meal.DoesNotExist:
#                 return redirect('error_page')
#         else:
#             return redirect('error_page')

#         Feedback.objects.create(user=request.user, rating=rating, comments=comments, **{item_type: item})

#         return redirect('feedback_success')

#     return render(request, 'chatbot/feedback_form.html', {'item_type': item_type, 'item_id': item_id})

# # Success view for feedback submission
# def feedback_success(request):
#     return render(request, 'chatbot/feedback_success.html')

# # Success view after setting preferences
# def preferences_success(request):
#     return render(request, 'chatbot/success.html')

def home_view(request):
    # Here, we will get data if necessary (e.g., workouts, meals), but based on your HTML,
    # we don't need any data for now, so it's kept simple.

    workouts = []  # Sample empty list, replace with your actual data retrieval logic
    meals = []     # Sample empty list, replace with your actual data retrieval logic

    # Render the home page with the necessary data (workouts, meals, etc.)
    return render(request, 'personalInfo/home.html', {'workouts': workouts, 'meals': meals})

def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        fitness_form = FitnessInformationForm(request.POST)

        if user_form.is_valid() and fitness_form.is_valid():
            # Save the user and hash the password
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password1'])
            user.save()

            # Save the fitness information and link it to the user
            fitness_info = fitness_form.save(commit=False)
            fitness_info.user = user
            fitness_info.save()

            # Log the user in after registration
            login(request, user)

            # Display a success message and redirect
            messages.success(request, 'Registration successful! Your fitness information has been saved.')
            return redirect('home')  # Adjust this redirect path to where you want the user to go after registration
        else:
            # If there are errors, send them back to the template
            error_message = "There was an error in your form submission."
            return render(request, 'chatbot/register.html', {
                'user_form': user_form,
                'fitness_form': fitness_form,
                'error': error_message
            })

    else:
        # Create empty forms if the request is GET
        user_form = RegistrationForm()
        fitness_form = FitnessInformationForm()

    return render(request, 'personalInfo/register.html', {
        'user_form': user_form,
        'fitness_form': fitness_form
    })
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to the dashboard or another page after successful login
        else:
            # Show an error message if authentication fails
            messages.error(request, 'Invalid username or password.')

    # Render the login form
    return render(request, 'personalInfo/login.html')
@login_required
def dashboard_view(request):
    return render(request, 'home/home.html')

def logout_view(request):
    logout(request)  # This will log the user out
    return render(request, 'personalInfo/logout.html')  # Render the logout page

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.db.models import Count

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Search for users with the provided email
        users_with_email = User.objects.filter(email=email)
        
        if users_with_email.count() == 1:
            # There is exactly one user with this email
            user = users_with_email.first()

            # Create token and uid for password reset link
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"{get_current_site(request).domain}/reset/{uid}/{token}/"

            # Send the password reset email
            send_mail(
                'Password Reset Request',
                f'Please click the link to reset your password: {reset_url}',
                'no-reply@cufitness.com',
                [email],
            )

            # Show success message
            messages.success(request, "Password reset email sent! Please check your inbox.")
            return redirect('login')
        
        elif users_with_email.count() > 1:
            # There are multiple users with this email
            messages.error(request, "Multiple users found with this email. Please contact support.")
            return render(request, 'personalInfo/forgot_password.html')

        else:
            # No users found with the given email
            messages.error(request, "No user found with this email address.")
            return render(request, 'personalInfo/forgot_password.html')  # Redirect back to the forgot password page

    return render(request, 'personalInfo/forgot_password.html')  # Show the forgot password form initially
