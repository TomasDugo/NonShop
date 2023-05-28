from django.db import models 

class Compradores(models.Model): 
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    mail = models.EmailField()


class Prendas(models.Model): 
    Tipo_Prenda = models.CharField(max_length=64)
    Color_Prenda = models.CharField(max_length=64)
    Precio = models.IntegerField()