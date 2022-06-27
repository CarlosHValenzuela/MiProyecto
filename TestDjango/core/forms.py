from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cuenta


class CuentaForm(ModelForm):

    class Meta:
        model = Cuenta
        fields=['idCuenta','nombreUsuario','contraUsuario','correoUsuario']