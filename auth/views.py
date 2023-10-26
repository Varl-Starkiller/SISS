from django.shortcuts import render

# Create your views here.
def authe(request):
    return render(request, 'signuplight.html')