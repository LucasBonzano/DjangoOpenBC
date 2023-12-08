from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html' , {})

def contacto(request):
    return render(request, 'contacto.html', {})

def carga(request):

    if request.method != 'GET':
        return HttpResponse("No se soporta el metodo POST")
    else:

        nombre = request.GET['nombre']
        apellido = request.GET['apellido']
        firma = request.GET['Firma']
        mensaje= request.GET['mensaje']
        return render(request, 'formulario/carga.html', {'nombre':nombre, 'apellido':apellido,'Firma':firma,'mensaje':mensaje})

def sobremi(request):
    return render(request, 'sobremi.html' , {})


        