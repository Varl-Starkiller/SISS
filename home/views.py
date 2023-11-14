# views.py
from django.shortcuts import render, redirect
from .models import posts


def upload_image(request):
    if request.method == 'POST':
        captions = request.POST.get('caption')
        image = request.FILES['image']  # Use 'image' instead of 'images'

        new_post = posts(caption=captions, image=image)  # Match the field name
        new_post.save()

    return render(request, 'createpost.html')


def caption(request):
    post_all = posts.objects.all()
    return render(request, 'home.html', {'post': post_all})
