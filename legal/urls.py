from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.login, name="login"),
    path('form', views.form, name="form"),
    path('tables', views.tables, name="tables"),
    path('forgot', views.forgot, name="forgot"),
]
