from django.db import models


class comentario(models.Model):
    
    # name=models. para declarar como quiero que se cree el valor en la tabla y tambien para dar los valores que quiero ingresar 
    name=models.CharField(max_length=255, null=False,)
    score = models.IntegerField( default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=50, default="Firma")
    
    
    '''
    para cada tipo de columna se deben modelar los datos con anterioridad o darle expecificaciones para que vayan a lo especifico y se le de buenos valores
    Esto tiene que tener una buena recollecion de datos previas para hacer un buen modelo en python ya que las tablas van a tener a estar orientadas a una especie de POO
    '''
    
    def __str__(self):
        return self.name
    
    
'''
de esta manera vamos a crear todos los modelos para la inscripción de datos y comparaciones es agrupar inyeccion de sql para crear tablas y columnas y la POO de python para el uso de las mismas.
'''
