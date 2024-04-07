from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.conf import settings


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True)
    rut = models.CharField(max_length=20, blank=True)
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
    rol = models.CharField(max_length=1, choices=ROLES, default='P')  
    groups = models.ManyToManyField(Group, related_name='usuario_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_user_permissions')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    


class Doctor(Usuario):
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Pago(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    receta_medica = models.ForeignKey('RecetaMedica', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.paciente} por receta {self.receta_medica} - Monto : {self.monto} "
    


class RecetaMedica(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100, choices=[
        ('ETS', 'Chequeo de ETS'),
        ('Embarazo', 'Chequeo de Embarazo'),
        ('Examenes', 'Examenes')
    ])
    fecha_emision = models.DateField()

    def __str__(self):
        return self.nombre
    


class examen(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre