from django.shortcuts import render

# Create your views here.

def InicioSesion(request):
    return render(request, 'core/InicioSesion.html')

def PaginaPrincipal(request):
    return render(request, 'core/PaginaPrincipal.html')

def Seguimiento(request):
    return render(request, 'core/Seguimiento.html')

def Suscribirse(request):
    return render(request, 'core/Suscribirse.html')

def Carrito(request):
    return render(request, 'core/Carrito.html')

def Historial(request):
    return render(request, 'core/Historial.html')

def TuCuenta(request):
    return render(request, 'core/TuCuenta.html')