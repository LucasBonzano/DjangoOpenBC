from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Mundo")

def chau(request):
    return HttpResponse("Chau")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse ("Es Mayor de edad")
    else: 
        return HttpResponse ("Es menor de edad")
    
def Home(request):
    return render(request, 'html/index.html', {})

def dinamico(request, name):
    categories = ['codigo', 'marketing', 'diseño']
    context = {'name' : name, 'categories' : categories }
    return render(request, 'html/dinamico.html', context)