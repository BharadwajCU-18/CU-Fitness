from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Home page (Welcome)
def home_view(request):
    return render(request, 'personalInfo/home.html')

# Register page
def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegistrationForm()
    return render(request, 'personalInfo/register.html', {'form': form})

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
    return render(request, 'personalInfo/dashboard.html')

# Logout
def logout_view(request):
    logout(request)
    return render(request, 'personalInfo/logout.html')
