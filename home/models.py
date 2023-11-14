from django.db import models


# Create your models here.

class posts(models.Model):
    caption = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', null=True, default=None)

    # image

    class Meta:
        app_label = 'home'
