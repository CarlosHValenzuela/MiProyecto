from django.db import models

# Create your models here.

class Cuenta(models.Model):
    idCuenta = models.IntegerField(primary_key=True, verbose_name="Id de la cuenta")
    nombreUsuario = models.CharField(max_length=100, verbose_name="Nombre de la cuenta")
    contraUsuario = models.CharField(max_length=100, verbose_name="Contraseña de la cuenta")
    correoUsuario = models.CharField(max_length=200, verbose_name="Correo de la cuenta")

    def __str__(self):
        return self.nombreUsuario
