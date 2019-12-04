from django.urls import path
from django.contrib.auth import views, forms

from amigos import views

# Name space para configurar el espacio de nombres de la aplicación
# Usada con la etiqueta de los templates {% url %}
app_name = 'amigos'

urlpatterns = [path('', views.index, name='index')]
