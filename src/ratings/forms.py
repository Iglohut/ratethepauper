from django import forms

from .models import (
    LivingAspects,
    AspectRatings
)


class RatingForm(forms.ModelForm):
    comment = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={"placeholder": "Explain thyself... (optional)"}))

    rating = forms.IntegerField(label='')

    class Meta:
        model = AspectRatings
        fields = ['title', 'rating', 'comment']
