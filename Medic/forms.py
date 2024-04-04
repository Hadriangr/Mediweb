from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.core.exceptions import ValidationError
import re



def validar_rut(value):
    # Expresión regular para validar el formato del rut
    rut_regex = r'^\d{7,8}-[\dKk]$'
    if not re.match(rut_regex, value):
        raise ValidationError('El formato del rut no es válido.')



class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=255)
    telefono_contacto = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField()
    rut = forms.CharField(max_length=12, validators=[validar_rut])  # Modificar el tamaño máximo y agregar el validador

    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'apellido', 'email', 'direccion', 'telefono_contacto', 'fecha_nacimiento', 'rut', 'password1', 'password2')



