from django.shortcuts import render
from django.http import HttpResponse
from .models import comentario

# Create your views here.

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    """comentario1 = comentario(name = "Lucas", score = 10, comment = "Que giles que son los gatos")
    comentario1.save()
    """
    comentario2 = comentario.objects.create(name="Alex")  
    return HttpResponse("Ruta para probar crear modelos de datos")

def delete(request):
    
    comentario2 = comentario.objects.get(id=1)  
    comentario2.delete()
    return HttpResponse("Ruta para probar eliminar modelos de datos")
