# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .forms import RegistrationForm

# # Home page (Welcome)
# def home_view(request):
#     return render(request, 'personalInfo/home.html')

# # Register page
# def register_view(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  
#     else:
#         form = RegistrationForm()
#     return render(request, 'personalInfo/register.html', {'form': form})

# # Login page
# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Redirects to dashboard after login
#         else:
#             return render(request, 'personalInfo/login.html', {'error': 'Invalid credentials'})
#     return render(request, 'personalInfo/login.html')

# # Dashboard (Only for logged-in users)
# @login_required
# def dashboard_view(request):
#     return render(request, 'personalInfo/dashboard.html')

# # Logout
# def logout_view(request):
#     logout(request)
#     return render(request, 'personalInfo/logout.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, FitnessInformationForm
from .forms import RegistrationForm
from django.http import JsonResponse


# Home page (Welcome)
def home_view(request):
    # return render(request, 'personalInfo/home.html')
    return render(request, 'home/home.html')

# Register page → Redirect to Fitness Information Page
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fitnessInformation')
    else:
        form = RegistrationForm()
    return render(request, 'personalInfo/register.html', {'form': form})

# fitnessInformation page
def fitnessInformation_view(request):
    if request.method == "POST":
        form = FitnessInformationForm(request.POST)
        if form.is_valid():
            fitness_info = form.save(commit=False)
            fitness_info.user = request.user  # Associate fitness info with logged-in user
            fitness_info.save()
            return redirect('login')  # Redirect to login page after form submission
    else:
        form = FitnessInformationForm()

    return render(request, 'personalInfo/fitnessInformation.html', {'form': form})
def fitnessInformation_view(request):
    if request.method == "POST":
        return redirect('login')  
    return render(request, 'personalInfo/fitnessinformation.html')

# Login page
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirects to dashboard after login
        else:
            return render(request, 'personalInfo/login.html', {'error': 'Invalid credentials'})
    return render(request, 'personalInfo/login.html')

# Dashboard (Only for logged-in users)
@login_required
def dashboard_view(request):
    # return render(request, 'personalInfo/dashboard.html')
    return render(request, 'home/home.html')

# Logout
def logout_view(request):
    logout(request)
    return render(request, 'personalInfo/logout.html')

