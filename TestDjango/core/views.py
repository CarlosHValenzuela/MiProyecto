from django.shortcuts import render,redirect
from .forms import CuentaForm
from .models import Cuenta

# Create your views here.

def InicioSesion(request):

    datos = {
        'form': CuentaForm()

    }
    if request.method== 'POST':
        formulario = CuentaForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Guardados"

    return render(request, 'core/InicioSesion.html',datos)

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

    cuentas= Cuenta.objects.all()

    datos = {
        'cuentas': cuentas
    }
    return render(request, 'core/TuCuenta.html',datos)

def ModificarCuenta(request,id):

    cuenta = Cuenta.objects.get(idCuenta=id)

    datos = {
        'form':CuentaForm(instance=cuenta)

    }

    if request.method == 'POST':
        formulario = CuentaForm(data=request.POST,instance=cuenta)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificacion realizada"


    return render(request, 'core/ModificarCuenta.html', datos)

def EliminarCuenta(request,id):
    cuenta = Cuenta.objects.get(idCuenta=id)

    cuenta.delete()

    return redirect(to="TuCuenta")