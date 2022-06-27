from urllib import request
from django.shortcuts import render,redirect
from .forms import CuentaForm, ProductoForm
from .models import Cuenta, Producto

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
    productos= Producto.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'core/Seguimiento.html',datos)

def Suscribirse(request):
    return render(request, 'core/Suscribirse.html')



def Carrito(request):

    datos = {
        'form': ProductoForm()

    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Productos Guardados"

    return render(request, 'core/Carrito.html',datos)



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


def ModificarProducto(request,id):

    producto = Producto.objects.get(idProducto=id)

    datos = {
        'form':ProductoForm(instance=producto)

    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificacion realizada"

    return render (request, 'core/ModificarProducto.html', datos)


def EliminarProducto(request,id):
    producto = Producto.objects.get(idProducto=id)

    producto.delete()

    return redirect(to="Seguimiento")
