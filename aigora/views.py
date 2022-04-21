from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.


def index(request):
    return render(request, 'home.html')


def signup(request):
    forms = UserRegisterForm()
    return render(request, 'registration/signup.html', {'forms': forms})


@login_required(login_url='login')
def display(request):
    return render(request, 'display.html')
