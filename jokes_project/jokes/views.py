from django.shortcuts import render
from django.http import JsonResponse
import requests
import random

def index(request):

    return render(request, 'index.html')

def random_number_api(request):
    random_number = random.randint(1, 100)
    data = {
        'random_number': random_number
    }
    return JsonResponse(data)

