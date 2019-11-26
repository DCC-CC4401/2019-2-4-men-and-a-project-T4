from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
#


class PerfilUsuario(models.Model):
    # Datos del usuario
    usuario = models.OneToOneField(User, related_name='PerfilUsuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(max_length=256, unique=True)
    foto_perfil = models.ImageField(upload_to='fotos', default='fotos/aceitunas.jpg')

    # Atributos para manejo de amigos y solicitudes
    amigos = models.ManyToManyField('self')
    solicitudes = models.ManyToManyField('self')

    def extraerActividadesSemanales(self, start_of_week):
        end_week = start_of_week + datetime.timedelta(7)
        entries = Actividades.objects.filter(user_id=self, h_inicio__range=[start_of_week, end_week])
        return entries

    def extraerEstadisticasSemanales(self, start_of_week):
        activities = self.extraerActividadesSemanales(start_of_week)
        dictionary = {}
        categories = Categoria.objects.all()
        for category in categories:
            dictionary[category.c_nombre] = datetime.timedelta(hours=0, minutes=0, seconds=0)
        for activity in activities:
            hour = activity.duracion.hour
            minute = activity.duracion.minute
            second = activity.duracion.second
            dictionary[activity.categoria.c_nombre] += datetime.timedelta(hours=hour, minutes=minute, seconds=second)
        return dictionary


class Categoria(models.Model):
    c_nombre = models.CharField(max_length=200)


class Actividades(models.Model):
    user_id = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    h_inicio = models.DateTimeField()
    duracion = models.TimeField(null=True)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)


class Plantilla(models.Model):
    user_id = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
