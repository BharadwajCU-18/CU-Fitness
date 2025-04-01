from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, FitnessInformationForm
# from .models import FitnessInformation<<<<<<< HEAD
from django.http import JsonResponse



# Home page (Welcome)
def home_view(request):
    return render(request, 'personalInfo/home.html')

# Register page → Redirect to Login page after successful registration
def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        fitness_form = FitnessInformationForm(request.POST)
        
        # Check if the username already exists
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'personalInfo/register.html', {'user_form': user_form, 'fitness_form': fitness_form, 'error': 'Username already exists'})

        if user_form.is_valid() and fitness_form.is_valid():
            # Save user data
            user = user_form.save()

            # Save fitness info and associate it with the user
            fitness_info = fitness_form.save(commit=False)
            fitness_info.user = user
            fitness_info.save()

            # Automatically log the user in after registration
            login(request, user)

            return redirect('home')  # Redirect to the home page or dashboard

    else:
        user_form = RegistrationForm()
        fitness_form = FitnessInformationForm()

    return render(request, 'personalInfo/register.html', {'user_form': user_form, 'fitness_form': fitness_form})

# Login page
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirects to the home page after login
        else:
            return render(request, 'personalInfo/login.html', {'error': 'Invalid credentials'})
    return render(request, 'personalInfo/login.html')

# Dashboard (Only for logged-in users)
@login_required
def dashboard_view(request):
    return render(request, 'home/home.html')

# Logout
def logout_view(request):
    logout(request)
    return render(request, 'personalInfo/logout.html')
# def chatbot_home(request):
#     return render(request, 'personalinfo/chatbot.html')

# def chatbot_response(request):
#     user_message = request.GET.get("message", "").lower()

#     # Define some basic responses
#     if "workout" in user_message:
#         response = "What kind of workout are you looking for? (e.g., cardio, strength, flexibility)"
#     elif "beginner" in user_message:
#         response = "For beginners, I suggest 3 sets of 10 push-ups, 15-minute cardio, and stretching exercises."
#     elif "nutrition" in user_message:
#         response = "For good nutrition, try eating lean proteins, vegetables, and whole grains."
#     elif "motivational" in user_message:
#         response = "Keep going! Your effort will pay off. You’re doing great!"
#     else:
#         response = "I’m here to help you with fitness plans and tips! How can I assist you today?"

#     return JsonResponse({"response": response})
# personalinfo/views.py


# openai.api_key = settings.OPENAI_API_KEY


# Set up OpenAI API key
# openai.api_key = settings.OPENAI_API_KEY



# def generate_session_id():
#     return str(uuid.uuid4())  # Generate a unique session ID using UUID




# Make sure you have your OpenAI API key set up correctly.


