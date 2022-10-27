from django.shortcuts import render


def login(request):
    return render(request, 'legal/login.html')


def home(request):
    return render(request, 'legal/home.html')


def tables(request):
    return render(request, 'legal/tables.html')


def form(request):
    return render(request, 'legal/form.html')


def forgot(request):
    return render(request, 'legal/forgotps.html')
