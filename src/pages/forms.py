from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    comment = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={"placeholder": "You what you thinking about..?"}))
    name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={"placeholder": "Name"}))

    email = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={"placeholder": "youremail@something.com"}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'comment']
