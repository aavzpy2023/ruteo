from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

# def login(request):
#     """ Login page """
#     context = {
#         'username': '',
#         'password': ''
#                }
#     return render(request, "registration/login.html", context)

@login_required
def home(request):
    """ Login page """
    template = loader.get_template("home/index.html")
    context = { "title": "Rutas de distribución de artículos"}
    return HttpResponse(template.render(context, request))
    # return render(request, "node/node.html")
    # return render(request, "base1.html")

@login_required
def node(request):
    """ Node page"""
    # template = loader.get_template("home/crud.html")
    context = { "title": "Rutas de distribución de artículos"}
    # return HttpResponse(template.render(context, request))
    return render(request, 'crud/crud.html', context)

def logout(request):
    """ Logout page """
    logout(request)
    return redirect("home")
