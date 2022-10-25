from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, 'legal/login.html')


def home(request):
    return render(request, 'legal/home.html')


def registro(request):
    return render(request, 'legal/registro.html')
