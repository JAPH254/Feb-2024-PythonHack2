from django.shortcuts import render
import requests
import os

def home(request):
    # Retrieve location from user input (replace with appropriate method)
    location = request.GET.get('location')

    # Validate location input (optional, but recommended for robustness)
    if not location:
        context = {'error': 'Please enter a valid location.'}
        return render(request, 'templates/home.html', context)

    # Construct the API URL with a placeholder for the location
    url = 'https://weatherapi-com.p.rapidapi.com/current.json?q={}'

    # Set headers with your X-RapidAPI-Key (avoid exposing it in code)
    headers = {
        'X-RapidAPI-Host': 'weatherapi-com.p.rapidapi.com',
        'X-RapidAPI-Key': 'c91f9666e1msha2a78962a9ff863p1255ffjsnc55172833efb'
        # os.environ.get('YOUR_API_KEY')  # Access from environment variable
    }

    try:
        # Make the API request, handling potential errors gracefully
        response = requests.get(url.format(location), headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()
        context = {'data': data}
        return render(request, 'templates/home.html', context)

    except requests.exceptions.RequestException as e:
        context = {'error': f'An error occurred: {e}'}
        return render(request, 'templates/home.html', context)

def jokes(request):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json()
    context = {'joke': joke}
    return render(request, 'templates/home.html', context)