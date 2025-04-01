from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
@login_required
=======

>>>>>>> origin/main
def home_view(request):
    return render(request, 'home.html')