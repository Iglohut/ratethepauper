from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    comment = models.TextField(max_length=500)

    def get_absolute_url(self):
        return '/'
