from django import forms
from .models import Profile

class EditProfile(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    bio = forms.CharField(widget = forms.Textarea)
    location = forms.CharField()
    birth_date = forms.DateField(widget = forms.DateInput(attrs = {'type':'date'}))
    email = forms.EmailField()
