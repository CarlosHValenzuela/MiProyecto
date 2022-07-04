from pyexpat import model
from django.db import models

# Create your models here.

class Cuenta(models.Model):
    idCuenta = models.IntegerField(primary_key=True, verbose_name="Id de la cuenta")
    nombreUsuario = models.CharField(max_length=100, verbose_name="Nombre de la cuenta")
    contraUsuario = models.CharField(max_length=100, verbose_name="Contraseña de la cuenta")
    correoUsuario = models.CharField(max_length=200, verbose_name="Correo de la cuenta")

    def __str__(self):
        return self.nombreUsuario

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id del producto")
    nombreProducto = models.CharField(max_length=100, verbose_name="Nombre del producto")
    precio = models.IntegerField(verbose_name="Precio del producto")
    direccionCasa = models.CharField(max_length=250, verbose_name="Dirrecion del comprador")

    def __str__(self):
        return self.nombreProducto

class Suscripcion(models.Model):
    idSuscripcion = models.IntegerField(primary_key=True, verbose_name="Id de la suscripcion")
    nombreCliente = models.CharField(max_length=250,verbose_name="Nombre del suscriptor")

    def __str__(self):
        return self.nombreCliente


