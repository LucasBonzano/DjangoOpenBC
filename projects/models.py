from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    asistencia = models.CharField(max_length=100)
    linkQR = models.CharField(max_length=100)
    codigodeaccesoQR = models.CharField(max_length=100)
    
    