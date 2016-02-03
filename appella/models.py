from __future__ import unicode_literals
from django.db import models

# Create your models here.
'''
AREA (id, latitud1, longitud1,latitud2, longitud2, latitud3, longitud3, latitud4, longitud4)
USUARIO (id, nombre, ap_paterno, ap_materno, telefono, imagen, area)
EXPEDIENTE (id, estado)
ZONA (id, latitud, longitud, area)
PERDIDO (id, fecha, img, texto, usuario, expediente)
ENCONTRADO (id, fecha, img, texto, usuario, expediente)
'''
class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    ar_lat1 = models.CharField(max_length=25)
    ar_lon1 = models.CharField(max_length=25)
    ar_lat2 = models.CharField(max_length=25)
    ar_lon2 = models.CharField(max_length=25)
    ar_lat3 = models.CharField(max_length=25)
    ar_lon3 = models.CharField(max_length=25)
    ar_lat4 = models.CharField(max_length=25)
    ar_lon4 = models.CharField(max_length=25)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    us_nombre = models.CharField(max_length=25)
    us_ap_paterno = models.CharField(max_length=25)
    us_ap_materno = models.CharField(max_length=25)
    us_telefono = models.CharField(max_length=20)
    us_img = models.FileField(upload_to="media/%Y%m%d_%H-%M-%s")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="tiene muchos")

class Expediente(models.Model):
    id_expediente = models.AutoField(primary_key=True)
    ex_estado = models.CharField(max_length=25)

class Zona(models.Model):
    id_zona = models.AutoField(primary_key=True)
    zo_lat = models.CharField(max_length=25)
    zo_lon = models.CharField(max_length=25)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="tiene muchos")

class Perdido(models.Model):
    id_perdido = models.AutoField(primary_key=True)
    pe_fecha = models.CharField(max_length=25)
    pe_img = models.FileField(upload_to="media/%Y%m%d_%H-%M-%s")
    pe_texto = models.CharField(max_length=140)
    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE, verbose_name="tiene un")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="tiene muchos")

class Encontrado(models.Model):
    id_encontrado = models.AutoField(primary_key=True)
    en_fecha = models.CharField(max_length=25)
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