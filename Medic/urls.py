"""
URL configuration for mediweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('pago/<int:pago_id>/', views.detalle_pago, name='detalle_pago'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('examenes-hombre/', views.examenes_hombre, name='examenes_hombre'),
    path('examenes-mujer/', views.examenes_mujer, name='examenes_mujer'),
    path('cuadro-1/', views.Mcuadro_1, name='Mcuadro_1'),
    path('cuadro-2/', views.Mcuadro_2, name='Mcuadro_2'),
    path('cuadro-3/', views.Mcuadro_3, name='Mcuadro_3'),
    path('cuadro-4/', views.Mcuadro_4, name='Mcuadro_4'),
]
