from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaPrincipal, name="PaginaPrincipal"),
    path('Seguimiento', Seguimiento,name="Seguimiento"),
    path('Suscribirse', Suscribirse, name="Suscribirse"),
    path('Carrito', Carrito, name="Carrito"),
    path('Historial', Historial, name="Historial"),
    path('TuCuenta', TuCuenta, name="TuCuenta"),
    path('InicioSesion',InicioSesion, name="InicioSesion"),
    path('ModificarCuenta/<id>',ModificarCuenta, name="ModificarCuenta"),
    path('EliminarCuenta/<id>',EliminarCuenta, name="EliminarCuenta"),
    path('ModificarProducto/<id>',ModificarProducto, name="ModificarProducto"),
    path('EliminarProducto/<id>',EliminarProducto, name="EliminarProducto"),
    path('NuevaSuscripcion', NuevaSuscripcion, name="NuevaSuscripcion"),
    path('ModificarSuscripcion/<id>',ModificarSuscripcion, name="ModificarSuscripcion"),
    path('EliminarSuscripcion/<id>',EliminarSuscripcion, name="EliminarSuscripcion"),
]