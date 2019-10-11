from django.db import models

# Create your models here.
from django.conf import settings
# from django.db import models
# from django.urls import reverse

# Make a model that has all objects to rate in there


class LivingAspects(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to='images/objects', null=True, blank=True)
    description = models.TextField(blank=True, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)


# Make a model that stores all ratings


