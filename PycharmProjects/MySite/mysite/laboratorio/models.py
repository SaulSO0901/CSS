from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion= models.CharField(max_length=200)

class Personal(models.Model):
    nombre=models.CharField(max_length=200)
    correo=models.CharField(max_length=200)
    telefono=models.CharField(max_length=200)

class Prestamo(models.Model):
    equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    personal=models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha_Prestamo=models.DateTimeField()
    echa_Devolucion=models.DateTimeField()
