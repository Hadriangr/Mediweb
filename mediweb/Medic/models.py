from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    direccion = models.CharField(max_length=255, blank=True)
    numero_seguro_social = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono_contacto = models.CharField(max_length=20, blank=True)
    genero_choices = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    genero = models.CharField(max_length=1, choices=genero_choices, blank=True)
    historial_medico = models.TextField(blank=True)
    imagen_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)
    ROLES = (
        ('P', 'Paciente'),
        ('D', 'Doctor'),
        ('A', 'Administrador'),
    )
    rol = models.CharField(max_length=1, choices=ROLES, default='P')  # Por defecto, se establece como paciente

    def __str__(self):
        return self.username
    



class doctor(AbstractUser):
    especialidad = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)

    def __str__(self):
        return(self.username)


class Pago(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    receta_medica = models.ForeignKey('RecetaMedica', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.paciente} por receta {self.receta_medica} - Monto : {self.monto} "