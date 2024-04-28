from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
import requests
import os
from . models import user
from .forms import CustomUserCreationForm
def home(request):
    location = request.GET.get('location')
    if not location:
        context = {'error': 'Please enter a valid location.'}
        return render(request, 'templates/home.html', context)
    url = 'https://weatherapi-com.p.rapidapi.com/current.json?q={}'
    headers = {
        'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
        'X-RapidAPI-Key': 'c91f9666e1msha2a78962a9ff863p1255ffjsnc55172833efb'
    }

    try:
        response = requests.get(url.format(location), headers=headers)
        response.raise_for_status()

        data = response.json()
        context = {'data': data}
        return render(request, 'templates/home.html', context)

    except requests.exceptions.RequestException as e:
        context = {'error': f'An error occurred: {e}'}
        return render(request, 'templates/home.html', context)
    
def jokes(request):
    res = requests.get('https://api.chucknorris.io/jokes/random')  
    joke = res.json()
    context = {'joke': joke}
    return render(request, 'templates/jokes.html', context)


def register(request):
    if request.method == 'POST':
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request,'templates/signup.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            context = {'error_message': error_message}
            return render(request, 'templates/login.html', context)
    else:
        context = {}
    return render(request, 'templates/login.html', context)
def base(request):
    return render(request, 'templates/base.html')
def logout(request):
    logout(request)
    return redirect('login')
