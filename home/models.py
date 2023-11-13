from django.db import models


# Create your models here.

class Fpost(models.Model):
    caption = models.CharField(max_length=1000)

    # image
    class Meta:
        app_label = 'home'
