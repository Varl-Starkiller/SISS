# views.py
# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .models import Users

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user using the User model
        new_user = Users(first_name=first_name, last_name=last_name, email=email, password=password)
        new_user.save()

    return render(request, 'signuplight.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # If authentication successful, log the user in
            login(request, user)
            # Redirect to a success page or any other desired page
            return redirect('success_page')
        else:
            # Authentication failed
            # You may want to handle unsuccessful login attempts, e.g., display an error message
            return render(request, 'signuplight.html', {'error_message': 'Invalid login credentials'})
    else:
        # For GET requests, render the signin form
        return render(request, 'signin.html')
