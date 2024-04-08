from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").upper()
    rut_sin_dv = rut[:-1]
    dv = rut[-1]
    suma = 0
    multiplo = 2
    for digito in reversed(rut_sin_dv):
        suma += int(digito) * multiplo
        multiplo += 1
        if multiplo > 7:
            multiplo = 2
    dv_calculado = 11 - (suma % 11)
    if dv_calculado == 10:
        dv_calculado = 'K'
    elif dv_calculado == 11:
        dv_calculado = '0'
    if str(dv_calculado) == dv:
        return rut
    else:
        raise forms.ValidationError('RUT inválido.')

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=255)
    telefono_contacto = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField()
    rut = forms.CharField(max_length=12, validators=[validar_rut])  # Agregar el validador de RUT

    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'apellido', 'email', 'direccion', 'telefono_contacto', 'fecha_nacimiento', 'rut', 'password1', 'password2')
