from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, EmailForm, UpdateUserForm, UpdateProfileForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


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

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
                      [cd['recipient']])
            messageSent = True
    else:
        form = EmailForm()
    return render(request, 'display.html', {'form': form, 'messageSent': messageSent})


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request, ('Your profile was successfully updated!'))
            return redirect('profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})
