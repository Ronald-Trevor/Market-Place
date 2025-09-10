from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))