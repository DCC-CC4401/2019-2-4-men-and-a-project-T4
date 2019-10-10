from django.urls import path
from django.contrib.auth import views, forms

from timePlan import views

# Name space para configurar el espacio de nombres de la aplicación
# Usada con la etiqueta de los templates {% url %]

#name es lo que se busca en url en html
#path  lo que queda arriba en el navegador
urlpatterns = [path('', views.loginView, name='login'),
               path('landing_page/', views.landing_page, name='landing_page'),
               path('auth', views.auth, name='auth'),
               path('profile/', views.userProfile, name='profile'),
               ]
