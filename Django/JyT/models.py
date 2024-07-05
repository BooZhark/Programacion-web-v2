from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )
    
class Producto(models.Model):
    nombrep = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='productos', default='no_imagen.png') #no_imagen es la imagen por defecto, falta añadirla

    def __str__(self):
        return f'{self.nombrep} -> {self.precio}'
