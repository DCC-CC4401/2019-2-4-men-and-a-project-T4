from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, related_name='PerfilUsuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(max_length=256, unique=True)
    foto_perfil = models.ImageField(upload_to='fotos', default='fotos/aceitunas.jpg')
    num_actividades = models.IntegerField(default=0)


class Actividades(models.Model):
    user_id = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    h_inicio = models.DateTimeField()
    duracion = models.TimeField(null=True)
    categoria = models.CharField(max_length=50)


class Plantilla(models.Model):
    user_id = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
