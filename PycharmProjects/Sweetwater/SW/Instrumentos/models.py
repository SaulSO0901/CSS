from django.db import models

# Create your models here.
class instrumentos(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    nombre= models.CharField(max_length=200)
    tipo= models.CharField(max_length=200)
    precio=models.IntegerField(blank=True, null=True)

class ventas(models.Model):
    idventa = models.AutoField(primary_key=True,null=False)
    Total = models.IntegerField(blank=True, null=True)
    Fecha = models.DateTimeField()
