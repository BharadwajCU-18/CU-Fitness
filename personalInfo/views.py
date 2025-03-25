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
    return render(request, 'personalInfo/home.html')
    # return render(request, 'home/home.html')

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
            # return redirect('dashboard')  # Redirects to dashboard after login
            return redirect('home')
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
def chatbot_home(request):
    return render(request, 'personalinfo/chatbot.html')

def chatbot_response(request):
    user_message = request.GET.get("message", "").lower()

    # Define some basic responses
    if "workout" in user_message:
        response = "What kind of workout are you looking for? (e.g., cardio, strength, flexibility)"
    elif "beginner" in user_message:
        response = "For beginners, I suggest 3 sets of 10 push-ups, 15-minute cardio, and stretching exercises."
    elif "nutrition" in user_message:
        response = "For good nutrition, try eating lean proteins, vegetables, and whole grains."
    elif "motivational" in user_message:
        response = "Keep going! Your effort will pay off. You’re doing great!"
    else:
        response = "I’m here to help you with fitness plans and tips! How can I assist you today?"

    return JsonResponse({"response": response})

