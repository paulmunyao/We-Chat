from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'registration/signup.html')

@login_required(login_url='login')
def display(request):
    return render(request,'display.html')    