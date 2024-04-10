from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms.widgets import DateInput
from django.utils.translation import gettext_lazy as _
from .models import Usuario

# Validador de RUT
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
        raise forms.ValidationError(_('RUT inválido.'))

class RegistroForm(UserCreationForm):
    # Opciones de género
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    direccion = forms.CharField(label="Dirección", max_length=255)
    telefono_contacto = forms.CharField(label="Teléfono de Contacto", max_length=20)
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        help_text=_("Formato: AAAA-MM-DD")
    )
    rut = forms.CharField(
        label="RUT",
        max_length=12,
        validators=[validar_rut],
        help_text=_("Formato: 12345678-9"),
        widget=forms.TextInput(attrs={'placeholder': '12345678-9'})
    )
    genero = forms.ChoiceField(
        label="Género",
        choices=GENERO_CHOICES
    )

    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if Usuario.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso. Por favor, elija otro.')
        return username

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'email', 'direccion', 'telefono_contacto', 'fecha_nacimiento', 'rut', 'genero', 'password1', 'password2')
