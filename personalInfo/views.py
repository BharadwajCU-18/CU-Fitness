from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from personalInfo.forms import RegistrationForm, FitnessInformationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, FitnessInformationForm
from django.contrib import messages
from home.models import CommunityPost
import openai
import logging
import os


logger = logging.getLogger(__name__)

# Set your OpenAI API key from environment variable
openai.api_key = settings.OPENAI_API_KEY

def home_view(request):
    # Fetch community posts ordered by the most recent first
    posts = CommunityPost.objects.all().order_by('-created_at')
    
    # Fetch workouts and meals (replace with actual data retrieval logic if necessary)
    workouts = []  # Placeholder, replace with actual data retrieval logic
    meals = []     # Placeholder, replace with actual data retrieval logic

    # Render the home page with the necessary data (posts, workouts, meals, etc.)
    return render(request, 'personalinfo/home.html', {
        'posts': posts, 
        'workouts': workouts, 
        'meals': meals
    })

def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        fitness_form = FitnessInformationForm(request.POST)
        
        if user_form.is_valid() and fitness_form.is_valid():
            # Save user data first
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()  # Save the user instance
            
            # Now save the fitness data and link it to the user
            fitness_info = fitness_form.save(commit=False)
            fitness_info.user = user  # Link the fitness info to the user
            fitness_info.phone_number = user_form.cleaned_data['phone_number']  # Make sure phone number is passed
            fitness_info.save()  # Save the fitness information
            
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('profile')  # Redirect to profile page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
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
            return redirect('home')  # Redirect to the home page or dashboard after successful login
        else:
            # Add error message using Django's messages framework
            messages.error(request, 'Invalid username or password.')
            return render(request, 'personalInfo/login.html')  # Render the login page again with the error message
    
    return render(request, 'personalInfo/login.html')  # Render the login page when the request is GET
@login_required
def dashboard_view(request):
    return render(request, 'home/home.html')

def logout_view(request):
    logout(request)  # This will log the user out
    return render(request, 'personalInfo/logout.html')  # Render the logout page


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Search for users with the provided email
        users_with_email = User.objects.filter(email=email)
        
        if users_with_email.count() == 1:
            # There is exactly one user with this email
            user = users_with_email.first()

            # Send the password reset email
            send_password_reset_email(user, request)

            # Show success message
            messages.success(request, "Password reset email sent! Please check your inbox.")
            return redirect('forgot_password')  # Ensure this matches the URL name in urls.py
        
        elif users_with_email.count() > 1:
            # There are multiple users with this email
            messages.error(request, "Multiple users found with this email. Please contact support.")
            return render(request, 'personalInfo/forgot_password.html')

        else:
            # No users found with the given email
            messages.error(request, "No user found with this email address.")
            return render(request, 'personalInfo/forgot_password.html')

    return render(request, 'personalInfo/forgot_password.html')  # This renders the form initially



def send_password_reset_email(user, request):
    # Generate the uid and token for password reset
    uid = urlsafe_base64_encode(str(user.pk).encode())
    token = default_token_generator.make_token(user)
    
    # Render the email content from a template
    message = render_to_string(
        'personalInfo/password_reset_email.html',  # Your email template
        {
            'user': user,
            'protocol': request.scheme,
            'domain': request.get_host(),
            'uid': uid,
            'token': token,
        }
    )

    # Use `DEFAULT_FROM_EMAIL` explicitly to set the sender address
    try:
        send_mail(
            'Password Reset Request',
            message,  # The message contains the rendered HTML content
            settings.DEFAULT_FROM_EMAIL,  # Sender email
            [user.email],  # Recipient email
            fail_silently=False,
            html_message=message  # Add HTML version of the email for proper rendering
        )
        print("Password reset email sent successfully!")
    except Exception as e:
        print(f"Failed to send password reset email: {e}")


