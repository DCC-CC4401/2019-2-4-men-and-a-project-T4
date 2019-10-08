from django.shortcuts import render
from django.http import HttpResponse
from timePlan.models import Plantilla, PerfilUsuario, Actividades


def landing_page(request):
    username = None
    # Esto hace que deba mostrar el nombre al loguearse
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'timePlan/landingPage.html',
                  {'username': username})   #el tercer elemento es contexto, son las variables
            #a las que puede acceder el usuario