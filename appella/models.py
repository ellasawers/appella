from __future__ import unicode_literals
from django.db import models

# Create your models here.
'''
USUARIO (id, nombre, ap_paterno, ap_materno, telefono, imagen, area)
EXPEDIENTE (id, estado)
LOCALIZACION(id, longitud, latitud, fecha, usuario)
PERDIDO (id, fecha, img, texto, usuario, expediente)
ENCONTRADO (id, fecha, img, texto, usuario, expediente)
'''


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    us_nombre = models.CharField(max_length=25)
    us_ap_paterno = models.CharField(max_length=25)
    us_ap_materno = models.CharField(max_length=25)
    us_telefono = models.CharField(max_length=20)
    us_img = models.FileField(upload_to="media/%Y%m%d_%H-%M-%s")

class Localizacion(models.Model): 
    id_localizacion = models.AutoField(primary_key=True)
    loc_longitud = models.CharField(max_length=25)
    loc_latitud = models.CharField(max_length=25)
    loc_fecha = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="tiene un")

class Expediente(models.Model):
    id_expediente = models.AutoField(primary_key=True)
    ex_estado = models.CharField(max_length=25)

class Perdido(models.Model):
    id_perdido = models.AutoField(primary_key=True)
    pe_fecha = models.DateTimeField(auto_now_add=True)
    pe_img = models.FileField(upload_to="media/%Y%m%d_%H-%M-%s")
    pe_texto = models.CharField(max_length=140)
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, verbose_name="tiene un")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="tiene muchos")

class Encontrado(models.Model):
    id_encontrado = models.AutoField(primary_key=True)
    en_fecha = models.DateTimeField(auto_now_add=True)
    en_img = models.FileField(upload_to="media/%Y%m%d_%H-%M-%s")
    en_texto = models.CharField(max_length=140)
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, verbose_name="tiene un")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="tiene muchos")

'''
class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.titulo
'''