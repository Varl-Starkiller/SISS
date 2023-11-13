# forms.py
from django import forms
from .models import posts


class HotelForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['caption', 'image']
