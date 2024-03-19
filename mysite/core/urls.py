""" Core.urls """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    # path("account/login/", views.entrar, name="entrar"),
    path("rutas/", views.rutas, name="rutas"),
    path("distancias/", views.distancias, name="distancias"),
    path("farmacias/", views.farmacias, name="farmacias"),
    path("logout/", views.salir, name="salir"),
]
