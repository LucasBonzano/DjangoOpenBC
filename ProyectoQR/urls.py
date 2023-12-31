
from django.contrib import admin
from django.urls import path
from . import vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', vista.saludo, name= 'saludo'),
    path('chau/', vista.chau, name= 'chau'),
    path('adulto/', vista.adulto, name='adulto'),
    path('Home/', vista.Home, name='Home'),
    path('dinamico/', vista.dinamico, name='dinamico')
]
