from rest_framework import serializers
from core.models import Suscripcion

class SuscripcionSerializar(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['idSuscripcion','nombreCliente']