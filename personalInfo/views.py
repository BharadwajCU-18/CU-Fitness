from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, FitnessInformationForm
# from .models import FitnessInformation

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
