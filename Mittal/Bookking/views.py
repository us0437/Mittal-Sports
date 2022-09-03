import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home.html')

def login_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.info(request,'Username or Password is incorrect')

    context ={}
    return render(request, 'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    form  = CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)

def booking(request):
    return render(request,'booking.html')

def badminton(request):
    return render(request,'badminton.html')