from django.urls import path
from django.contrib.auth import views, forms

from . import views as app_views

# Name space para configurar el espacio de nombres de la aplicación
# Usada con la etiqueta de los templates {% url %]
app_name = 'timePlan'

urlpatterns = [path('', views.LoginView.as_view(template_name='timePlan/login.html',
                                                authentication_form=forms.AuthenticationForm,
                                                extra_context={'next': 'landing_page'}),
                    name='login'),
               path('landing_page/', app_views.landing_page, name='landing_page')]
