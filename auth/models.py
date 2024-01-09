from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

class Users(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=12)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'auth'
