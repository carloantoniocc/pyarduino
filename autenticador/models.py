from django.db import models

# Create your models here.

class Device(models.Model):
    nombre=models.CharField(max_length=30,default="Nombre")
    modelo=models.CharField(max_length=30, null=True)
    descripcion=models.CharField(max_length=30, null=True)
    token=models.CharField(max_length=50,null=True)
    activo= models.BooleanField(default=1)
    #fechacreacion=models.DateField()
