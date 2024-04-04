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
            return redirect('inicio')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})