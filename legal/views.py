from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import formularioCadastro


@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'legal/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)

            return render(request, 'legal/home.html')
        else:
            return render(request, 'Colocar pagina que está errado')


@csrf_exempt
def home(request):
    return render(request, 'legal/home.html')


@csrf_exempt
def tables(request):
    return render(request, 'legal/tables.html')


@csrf_exempt
def form(request):
    form = formularioCadastro(request.POST)
    if form.is_valid():
        form.save
    return render(request, 'legal/form.html', {'form': form})


@csrf_exempt
def forgot(request):
    return render(request, 'legal/forgotps.html')


@csrf_exempt
def register(request):
    if request.method == "GET":
        return render(request, 'legal/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe esse usuário.')

        user = User.objects.create_user(
            username=username, email=email, password=senha)
        user.save()

        return HttpResponse('usuário cadastrado com sucesso')
