from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageUploadForm
from timePlan.models import *
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='')
def landing_page(request):
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
        correo = usuario.nombre
        actividades_del_usuario = list(Actividades.objects.filter(user_id=usuario.id).values())

        for each in actividades_del_usuario:
            each['anho'] = int(each['h_inicio'].year)
            each['mes'] = int(each['h_inicio'].month)
            each['dia'] = int(each['h_inicio'].day)
            each['hora_inicio'] = int(each['h_inicio'].hour-3)
            each['hora_duracion'] = int(each['duracion'].hour)
            del each['h_inicio']
            del each['duracion']
            each = json.dumps(each).encode('utf8')

    return render(request, 'timePlan/LandingPage.html',
                  {'username': username,
                   'photo': foto,
                   'email': correo,
                   'activities': actividades_del_usuario})  # el tercer elemento es contexto, son las variables # a las que puede acceder el usuario

    # Esto hace que deba mostrar el nombre al loguearse


def loginView(request):
    return render(request, 'timePlan/login.html')


def handle_uploaded_file(f):
    with open('some/file/img_test.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_img(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = PerfilUsuario(image_field=request.FILES['file'])
            instance.model_pic = form.cleaned_data['image']
            instance.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ImageUploadForm()
    return render(request, 'timePlan/UserProfile.html', {'form': form})


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
        return render(request, 'timePlan/login.html')


@login_required(login_url='')
def userProfile(request):
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
    return render(request, 'timePlan/UserProfile.html',
                  {'username': username, 'photo': foto})


def logoutView(request):
    logout(request)
    return render(request, 'timePlan/login.html')
