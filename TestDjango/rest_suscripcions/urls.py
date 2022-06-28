from django import urls
from django.urls import URLPattern, path
from rest_suscripcions.views import lista_suscripciones

URLPatterns = [
    path('lista_suscripciones', lista_suscripciones, name="lista_suscripciones"),
]