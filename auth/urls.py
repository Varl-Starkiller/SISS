from django.urls import path, include

from . import views
urlpatterns = [
    path('login', views.login, name="Login"),
    path('register', views.registration, name='Registration'),
]
