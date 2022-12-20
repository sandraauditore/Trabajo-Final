from django.db import models

# Create your models here.


class Galeria(models.Model):

    Nombre = models.CharField(max_length=30)
    Imagen = models.ImageField(upload_to="galeria")
    Descripcion = models.CharField(max_length=120) 
    Precio = models.FloatField()

    def __str__(self) -> str:
        return f"{self.Nombre} - {self.Imagen} - {self.Descripcion} - ${self.Precio}"




class Contacto(models.Model):

    Nombre = models.CharField(max_length=30)
    Email = models.EmailField()
    Mensaje = models.CharField(max_length=100)
    


