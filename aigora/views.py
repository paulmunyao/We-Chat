from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,EmailForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def display(request):
    messageSent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Send an email with Django"
            message = cd['message']

            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['recipient']])
            messageSent = True
    else:
        form = EmailForm()
    return render(request, 'display.html',{'form':form, 'messageSent':messageSent})
