from django.contrib import admin
from .models import Cuenta, Producto,Suscripcion
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Producto)
admin.site.register(Suscripcion)