from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cuenta, Producto


class CuentaForm(ModelForm):

    class Meta:
        model = Cuenta
        fields=['idCuenta','nombreUsuario','contraUsuario','correoUsuario']

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields=['idProducto','nombreProducto','precio','direccionCasa']