from django.shortcuts import render
from .models import Usuario

def index(request):
    context = {
        "user": "",
    }
    return render(request, "pages/index.html", context)

def index(request):
    context = {}
    return render(request, "pages/contacto.html", context)

def index(request):
    context = {}
    return render(request, "pages/login.html", context)

def index(request):
    context = {}
    return render(request, "pages/monitores.html", context)

def index(request):
    context = {}
    return render(request, "pages/registro.html", context)

def index(request):
    context = {}
    return render(request, "pages/sbnosotros.html", context)

def index(request):
    context = {}
    return render(request, "pages/tarjvideo.html", context)

def index(request):
    context = {}
    return render(request, "pages/user_add.html", context)    