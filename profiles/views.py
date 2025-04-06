# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from .models import FitnessProfile
# from .forms import FitnessInformationForm
# from django.contrib.auth.decorators import login_required
# # from personalInfo.models import FitnessProfile   

# @login_required
# def my_profile(request):
#     profile, created = FitnessProfile.objects.get_or_create(user=request.user)

#     if request.method == 'POST':
#         form = FitnessInformationForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profiles:my_profile')
#     else:
#         form = FitnessInformationForm(instance=profile)

#     return render(request, 'profiles/profile_page.html', {'user_info': FitnessProfile})
#     #     # 'form': form,
#     #     # 'profile': profile,
#     # })


from django.shortcuts import render, redirect
from .forms import FitnessInformationForm
from .models import FitnessProfile

# View to display user's fitness profile
def profile_view(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if the user is not authenticated
    
    # Try to fetch the fitness profile for the logged-in user
    try:
        fitness_profile = FitnessProfile.objects.get(user=request.user)
    except FitnessProfile.DoesNotExist:
        fitness_profile = None  # If the profile doesn't exist, set it to None

    return render(request, 'profiles/profile.html', {'fitness_profile': fitness_profile})

# View to update user's fitness profile
def update_fitness_profile(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not authenticated
    
    # Try to fetch the user's existing fitness profile, or create a new one if it doesn't exist
    try:
        fitness_profile = FitnessProfile.objects.get(user=request.user)
    except FitnessProfile.DoesNotExist:
        fitness_profile = None  # If no profile exists, initialize it as None
    
    # If the request method is POST, handle form submission
    if request.method == 'POST':
        form = FitnessInformationForm(request.POST, instance=fitness_profile)
        if form.is_valid():
            form.save()  # Save the form data (update the profile)
            return redirect('profile')  # Redirect to profile page after saving
    else:
        # If GET request, pre-fill the form with the existing profile data
        form = FitnessInformationForm(instance=fitness_profile)

    return render(request, 'profiles/update_fitness_profile.html', {'form': form})
