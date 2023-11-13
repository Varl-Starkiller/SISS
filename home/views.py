from django.shortcuts import render

from home.models import Fpost


# Create your views here.

def npost(request):
    if request.method == "POST":
        new_post = Fpost()
        new_post.caption = request.POST.get('caption')

        if len(request.FILES) != 0:
            new_post.image = request.FILES['image']

        new_post.save()
    return render(request, 'home.html')
