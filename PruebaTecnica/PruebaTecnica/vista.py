from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html' , {})

def contacto(request):
    return render(request, 'contacto.html' , {})

def sobremi(request):
    return render(request, 'sobremi.html' , {})
        