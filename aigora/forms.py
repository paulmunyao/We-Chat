from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'email', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'password1', 'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'password2', 'class': 'form-control'}),
        }


class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('recipient', 'message')
        widgets = {
            'recipient': forms.EmailInput(attrs={'placeholder': 'recipient', 'class': 'form-control'}),
            'message': forms.TextInput(attrs={'placeholder': 'message', 'class': 'form-control'}),
        }


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=EmailInput(attrs={'class': 'form-control'}),
    )

    username = forms.CharField(
        max_length=255,
        required=True,
        widget=TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', )
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location', 'description']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'biograpghy'}),
            'location': forms.TextInput(attrs={'class': 'loca'}),
            'description': forms.Textarea(attrs={'class': 'descrip'}),
        }
