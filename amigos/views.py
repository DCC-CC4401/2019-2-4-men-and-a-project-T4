from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import PerfilUsuario

# Create your views here.
@login_required(login_url='')
def index(request):
    """
    Maneja la aceptación/rechazo de las solicitudes de amistad.
    """
    # Obtención de datos básicos del usuario
    perfil_usuario = request.user.PerfilUsuario
    username = perfil_usuario.nombre
    foto = perfil_usuario.foto_perfil

    if request.method == 'POST':
        try:
            correo_usuario, aceptado = request.POST['solicitante-aceptado'], True
        except KeyError:
            correo_usuario, aceptado = request.POST['solicitante-rechazado'], False

        # Se obtiene el usuario solicitante y se elimina de las solicitudes
        usuario_solicitante = get_object_or_404(PerfilUsuario, correo=correo_usuario)
        perfil_usuario.solicitudes.remove(usuario_solicitante)

        if aceptado:
            perfil_usuario.amigos.add(usuario_solicitante)

    context = {'username': username, 'photo': foto, 'perfil_usuario': perfil_usuario}

    return render(request, 'amigos/UserProfile.html', context)
