from django.urls import path
from .views import PaginaPrincipal, Seguimiento, Suscribirse, Carrito, Historial,TuCuenta,InicioSesion

urlpatterns = [
    path('',InicioSesion,name="InicioSesion"),
    path('Home', PaginaPrincipal,name="PaginaPrincipal"),
    path('Seguimiento', Seguimiento,name="Seguimiento"),
    path('Suscribirse', Suscribirse, name="Suscribirse"),
    path('Carrito', Carrito, name="Carrito"),
    path('Historial', Historial, name="Historial"),
    path('TuCuenta', TuCuenta, name="TuCuenta"),
]