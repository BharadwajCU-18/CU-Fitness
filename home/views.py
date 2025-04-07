from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommunityPostForm
# from .models import CommunityPost
@login_required

def home_view(request):
    return render(request, 'home.html')

def submit_community_post(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect if the user isn't logged in
    
    if request.method == "POST":
        form = CommunityPostForm(request.POST)
        if form.is_valid():
            # Attach the post to the current logged-in user
            post = form.save(commit=False)
            post.user = request.user  # Assign the logged-in user to the post
            post.save()  # Save the post

            return redirect('home')  # Redirect to the homepage to show the new post
    else:
        form = CommunityPostForm()

    return render(request, 'submit_community_post.html', {'form': form})