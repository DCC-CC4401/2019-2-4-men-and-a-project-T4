from django.contrib import admin
from .models import PerfilUsuario, Actividades, Plantilla, Categoria

# Register your models here.
admin.site.register(PerfilUsuario)
admin.site.register(Actividades)
admin.site.register(Plantilla)
admin.site.register(Categoria)

