from django.urls import path

from legal.views import home, login, registro

urlpatterns = [
    path('', login),
    path('home', home),
    path('registro', registro),
]
