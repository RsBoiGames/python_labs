from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'templates/index.html')

def hello(request):
    return HttpResponse('Привет, Мир!')
