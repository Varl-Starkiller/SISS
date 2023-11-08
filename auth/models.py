from django.db import models


# Create your models here.
class Nuser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    signup_date = models.DateTimeField(auto_now_add=True, db_column='date_joined')

    class Meta:
        app_label = 'auth'   # Specify the app name to which this model belongs
