""" Core.urls """
from django.urls import path
from . import views


urlpatterns = [
    # path("", views.login, name="login"),
    path("", views.home, name="home"),
    # path("account/login/", views.entrar, name="entrar"),
    # path("routes/", views.routes, name="rutas"),
    # path("street_sections/", views.street_sections, name="distancias"),
    path("nodos/", views.node, name="nodos"),
    # path("logout/", views.logout, name="salir"),
    # path("newlogin/", views.new_login, name="newlogin"),
]
