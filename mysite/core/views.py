""" Core.views """
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def home(request):
    """ Main page """
    context = {}
    return render(request, "main/home.html", context)


@login_required
def rutas(request):
    """ Routes page """
    context = {}
    return render(request, "rutas/rutas.html", context)

@login_required
def distancias(request):
    """ distancia page """
    context = {}
    return render(request, "distancias/distancias.html", context)

@login_required
def farmacias(request):
    """ farmacias page """
    context = {}
    return render(request, "farmacias/farmacias.html", context)

# @login_required
def entrar(request):
    """ Login page """
    return render(request, "registration/login.html")

def salir(request):
    """ Logout page """
    logout(request)
    return redirect("home")
