from django.db import models
from datetime import date

class autor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class entrada(models.Model):
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=255)
    texto=models.TextField()
    fecha=models.DateField(default=date.today)
    puntaje= models.IntegerField(default=5)

    def __str__(self):
        return self.titulo
    