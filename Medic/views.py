from django.shortcuts import render
from .models import Pago
from .forms import RegistroForm


def index(request):
    return render(request, 'index.html')

def home(request):
    # Aquí puedes agregar la lógica necesaria para obtener datos de la base de datos u otros procesamientos
    context = {
        'titulo': 'Página de inicio',
        'mensaje': 'Bienvenido a nuestra aplicación de órdenes médicas.'
    }
    return render(request, 'inicio.html', context)




def detalle_pago(request, pago_id):
    pago = Pago.objects.get(id=pago_id)
    return render(request, 'medic/mi_pagina.html', {'pago': pago})





def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('index')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})



def examenes_hombre(request):
    return render(request, 'examenes_hombre.html')




def examenes_mujer(request):
    cuadros = [
        {'titulo': 'Cuadro 1', 'contenido': 'Contenido del cuadro 1', 'ruta': 'Mcuadro_1'},
        {'titulo': 'Cuadro 2', 'contenido': 'Contenido del cuadro 2', 'ruta': 'Mcuadro_2'},
        {'titulo': 'Cuadro 3', 'contenido': 'Contenido del cuadro 3', 'ruta': 'Mcuadro_3'},
        {'titulo': 'Cuadro 4', 'contenido': 'Contenido del cuadro 4', 'ruta': 'Mcuadro_4'},
    ]
    return render(request, 'examenes_mujer.html', {'cuadros': cuadros})





def Mcuadro_1(request):
    return render(request, 'Mcuadro_1.html', {'titulo': 'Cuadro 1', 'contenido': 'Contenido del cuadro 1'})



def Mcuadro_2(request):
    return render(request, 'Mcuadro_2.html', {'titulo': 'Cuadro 2', 'contenido': 'Contenido del cuadro 2'})



def Mcuadro_3(request):
    return render(request, 'Mcuadro_3.html', {'titulo': 'Cuadro 3', 'contenido': 'Contenido del cuadro 3'})



def Mcuadro_4(request):
    return render(request, 'Mcuadro_4.html', {'titulo': 'Cuadro 4', 'contenido': 'Contenido del cuadro 4'})
