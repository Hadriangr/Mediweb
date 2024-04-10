from django.shortcuts import render,redirect
from .models import Pago,RecetaMedica,examen
from .forms import RegistroForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')



def detalle_pago(request, pago_id):
    pago = Pago.objects.get(id=pago_id)
    return render(request, 'medic/mi_pagina.html', {'pago': pago})



def mostrar_recetas_por_categoria(request, categoria):
    recetas = RecetaMedica.objects.filter(categoria=categoria)
    return render(request, 'mostrar_recetas.html', {'recetas': recetas, 'categoria': categoria})



def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('index')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'signup.html', {'form': form})




def render_cuadro(request, titulo, contenido, template_name):
    return render(request, template_name, {'titulo': titulo, 'contenido': contenido})



def examenes_mujer(request):
    # Recuperar las recetas médicas de la categoría "Examenes"
    examenes = RecetaMedica.objects.filter(categoria='Examenes')
    
    # Crear una lista de diccionarios con los datos necesarios para cada cuadro
    cuadros = []
    for examen in examenes:
        cuadro = {
            'titulo': examen.nombre,
            'contenido': examen.descripcion,
            'ruta': f'detalle_receta/{examen.id}',  # URL para ver los detalles de la receta
        }
        cuadros.append(cuadro)
    
    return render(request, 'examenes_mujer.html', {'cuadros': cuadros})



def examenes_hombre(request):
    cuadros = [
        {'titulo': 'Cuadro 1', 'contenido': 'Contenido del cuadro 1', 'ruta': 'Hcuadro_1'},
        {'titulo': 'Cuadro 2', 'contenido': 'Contenido del cuadro 2', 'ruta': 'Hcuadro_2'},
        {'titulo': 'Cuadro 3', 'contenido': 'Contenido del cuadro 3', 'ruta': 'Hcuadro_3'},
        {'titulo': 'Cuadro 4', 'contenido': 'Contenido del cuadro 4', 'ruta': 'Hcuadro_4'},
    ]
    return render(request, 'examenes_hombre.html', {'cuadros': cuadros})



def Mcuadro_1(request):
    return render_cuadro(request, 'Cuadro 1', 'Contenido del cuadro 1', 'Mcuadro_1.html')


def Mcuadro_2(request):
    return render_cuadro(request, 'Cuadro 2', 'Contenido del cuadro 2', 'Mcuadro_2.html')


def Mcuadro_3(request):
    return render_cuadro(request, 'Cuadro 3', 'Contenido del cuadro 3', 'Mcuadro_3.html')


def Mcuadro_4(request):
    return render_cuadro(request, 'Cuadro 4', 'Contenido del cuadro 4', 'Mcuadro_4.html')


def Hcuadro_1(request):
    return render_cuadro(request, 'Cuadro 1', 'Contenido del cuadro 1', 'Hcuadro_1.html')


def Hcuadro_2(request):
    return render_cuadro(request, 'Cuadro 2', 'Contenido del cuadro 2', 'Hcuadro_2.html')


def Hcuadro_3(request):
    return render_cuadro(request, 'Cuadro 3', 'Contenido del cuadro 3', 'Hcuadro_3.html')


def Hcuadro_4(request):
    return render_cuadro(request, 'Cuadro 4', 'Contenido del cuadro 4', 'Hcuadro_4.html')




class signupview(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'