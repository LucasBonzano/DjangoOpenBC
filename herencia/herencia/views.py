from django.http import HttpResponse
from django.shortcuts import render

def herencia(request):
    return render(request, 'herencia.html', {})

def bonzano(request):
    return render(request, 'bonzano.html', {})

def otravista(request):
    return render(request, 'otravista.html', {})

def index(request):
    return render(request, 'index.html', {})