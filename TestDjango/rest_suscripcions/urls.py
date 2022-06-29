from django import urls
from django.urls import URLPattern, path
from rest_suscripcions.views import lista_suscripciones,detalle_suscripcion
from rest_suscripcions.viewslogin import login

urlpatterns = [
    path('lista_suscripciones', lista_suscripciones, name="lista_suscripciones"),
    path('detalle_suscripcion/<id>', detalle_suscripcion, name="detalle_suscripcion"),
    path('login', login, name="login"),
]