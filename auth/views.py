from django.shortcuts import render

from auth.models import users


# Create your views here.
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = users(firstname=first_name, lastname=last_name, email=email, password=password)
        new_user.save()
    return render(request,  'signuplight.html')
