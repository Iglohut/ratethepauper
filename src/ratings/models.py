from django.db import models

# Create your models here.
from django.conf import settings
# from django.db import models
# from django.urls import reverse


# test list field from django.db import models
from typing import Iterable

# Costum helper-model to make ListFields in order to make hue's for later models


class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


# Make a model that has all objects to rate in there
class LivingAspects(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to='images/objects', null=True, blank=True)
    description = models.TextField(blank=True, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # input comma seperated: 1,2,3. Output: [1, 2 3]
    hues = ListField(blank=True, null=True)


# Make a model that stores all ratings
class AspectRatings(models.Model):
    title = models.CharField(max_length=120)  # Autofill in form
    rating = models.IntegerField(max_length=2, choices=[
                                 (i, i) for i in range(1, 11)])  # Choice by user
    # Choice by user, default in form is none?
    hue = models.CharField(max_length=20)
    comment = models.CharField(max_length=200)  # User may comment
    timestamp = models.DateTimeField(auto_now_add=True)
