from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageUploadForm
from timePlan.models import PerfilUsuario
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url='')
def landing_page(request):
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
        correo = usuario.nombre

    # Esto hace que deba mostrar el nombre al loguearse

    return render(request, 'timePlan/LandingPage.html',
                  {'username': username,
                   'photo': foto,
                   'email': correo})  # el tercer elemento es contexto, son las variables
    # a las que puede acceder el usuario


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
        return HttpResponse(request, 'fallas')


@login_required(login_url='')
def userProfile(request):
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
    return render(request, 'timePlan/UserProfile.html',
                  {'username': username, 'photo': foto})
