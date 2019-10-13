from django import forms

from .models import (
    LivingAspects,
    AspectRatings
)


class RatingForm(forms.ModelForm):
    class Meta:
        model = AspectRatings
        fields = ['title', 'rating', 'hue', 'comment']
