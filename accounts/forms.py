from django import forms
from django.contrib.auth.models import User


class loginForm(forms.ModelForm):
    model = User
    fields = ('username', 'password')