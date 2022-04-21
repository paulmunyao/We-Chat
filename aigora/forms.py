from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    widget = forms.EmailInput(attrs={'placeholder': 'email','class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'username','class': 'form-control'}),
            'password1':forms.PasswordInput(attrs={'placeholder': 'password1','class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'placeholder': 'password2','class': 'form-control'}),
        }
