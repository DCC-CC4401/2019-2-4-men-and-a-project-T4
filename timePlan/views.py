from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from timePlan.models import PerfilUsuario
from django.contrib.auth.decorators import login_required


@login_required(login_url='')
def landing_page(request):
    username = None
    # Esto hace que deba mostrar el nombre al loguearse
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'timePlan/LandingPage.html',
                  {'username': username})  # el tercer elemento es contexto, son las variables
    # a las que puede acceder el usuario


def loginView(request):
    return render(request, 'timePlan/login.html')


def auth(request):
    email = request.POST['correo']
    contrasena = request.POST['contrasena']
    django_user = PerfilUsuario.objects.get(correo=email).usuario
    nombre = PerfilUsuario.objects.get(correo=email).nombre
    username = django_user.username
    usuario = authenticate(username=username, password=contrasena)
    if usuario is not None:
        login(request, usuario)
        return landing_page(request)
    else:
        return HttpResponse(request, 'fallas')


@login_required(login_url='')
def userProfile(request):
    return render(request, 'timePlan/UserProfile.html')
