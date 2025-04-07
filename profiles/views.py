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
from django.contrib.auth.decorators import login_required
from personalInfo.models import FitnessInformation
from personalInfo.forms import FitnessInformationForm
from .models import FitnessProfile


@login_required
def profile_view(request):
    # Fetch the fitness profile for the logged-in user
    try:
        fitness_profile = FitnessInformation.objects.get(user=request.user)
    except FitnessInformation.DoesNotExist:
        fitness_profile = None  # Handle the case where the profile doesn't exist
    
    return render(request, 'profiles/profile.html', {
        'fitness_profile': fitness_profile,
    })


# View to update the user's fitness profile
@login_required
def update_fitness_profile(request):
    # Try to fetch the user's existing fitness profile
    try:
        fitness_profile = FitnessInformation.objects.get(user=request.user)
    except FitnessInformation.DoesNotExist:
        # If no profile exists, create a new one
        fitness_profile = FitnessInformation(user=request.user)

    # Handle form submission (POST request)
    if request.method == 'POST':
        form = FitnessInformationForm(request.POST, instance=fitness_profile)
        if form.is_valid():
            form.save()  # Save the updated fitness profile
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        # If it's a GET request, pre-fill the form with the existing profile data
        form = FitnessInformationForm(instance=fitness_profile)

    return render(request, 'profiles/update_fitness_profile.html', {'form': form})