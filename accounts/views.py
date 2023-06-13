from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(username=cd['username']):
                messages.error(request, "This username is already taken", 'danger')
            elif User.objects.filter(email=cd['email']):
                messages.error(request, "This email is already registered", 'danger')
            else:
                User.objects.create_user(cd['username'], cd['email'], cd['password'])
                messages.success(request, 'You registered successfully', 'success')
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You log in successfully', 'success')
                return redirect('task_lists')
            else:
                messages.error(request, 'your password or username is invalid!', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def logout(request):
    django_logout(request)
    messages.success(request, 'You Logout successfully', 'success')
    return redirect('login')