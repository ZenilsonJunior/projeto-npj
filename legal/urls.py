from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="legal-login"),
    path('home/', views.home, name="legal-home"),
    path('registro', views.registro, name="legal-registro"),
]
