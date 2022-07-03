from django import forms
from .models import Newsletter


class NewsletterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField()

