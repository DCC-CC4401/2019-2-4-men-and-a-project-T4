from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from timePlan.models import PerfilUsuario
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json


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
        test = form.is_valid()
        if form.is_valid():
            m = request.user.PerfilUsuario
            m.foto_perfil = form.cleaned_data['image']
            m.save()
    return redirect(reverse('profile'))


def auth(request):
    email = request.POST['correo']
    contrasena = request.POST['contrasena']
    try:
        django_user = PerfilUsuario.objects.get(correo=email).usuario
    except PerfilUsuario.DoesNotExist:
        django_user = None
    if django_user is not None:
        username = django_user.username
        usuario = authenticate(username=username, password=contrasena)
        if usuario is not None:
            login(request, usuario)
            return redirect(reverse('landing_page'))
    return redirect(reverse('login'))


@login_required(login_url='')
def userProfile(request):
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        correo = usuario.correo
        foto = usuario.foto_perfil
    return render(request, 'timePlan/UserProfile.html',
                  {'username': username, 'photo': foto, 'correo': correo})


def logoutView(request):
    logout(request)
    return redirect(reverse('login'))


def userRegister(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        test = form.is_valid()
        if test:
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['correoR'],
                    email=form.cleaned_data['correoR'],
                    password=form.cleaned_data['contrasenaR'],
                )
                PerfilUsuario.objects.create(
                    usuario=user,
                    nombre=form.cleaned_data['usuario'],
                    correo=form.cleaned_data['correoR'],
                    foto_perfil=form.cleaned_data['image'],
                )
            except IntegrityError as I:
                return HttpResponse('Correo ya registrado')
    return redirect(reverse('login'))


@login_required(login_url='')
def security(request):
    """
    Únicamente muestra el template Security.html.
    """
    # Obtengo los datos del usuario
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
        correo = usuario.nombre

    # Creo la variable contexto
    context = {'username': username, 'photo': foto, 'email': correo}

    return render(request, 'timePlan/Security.html', context)


@login_required(login_url='')
def friends(request):
    """
    Únicamente muestra el template Friends.html.
    """
    # Obtengo los datos del usuario
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
        correo = usuario.nombre

    # Creo la variable contexto
    context = {'username': username, 'photo': foto, 'email': correo}

    return render(request, 'timePlan/Friends.html', context)


@login_required(login_url='')
def my_activities(request):
    """
    Únicamente muestra el template MyActivities.html.
    """
    # Obtengo los datos del usuario
    if request.user.is_authenticated:
        usuario = request.user.PerfilUsuario
        username = usuario.nombre
        foto = usuario.foto_perfil
        correo = usuario.nombre

    # Creo la variable contexto
    context = {'username': username, 'photo': foto, 'email': correo}

    return render(request, 'timePlan/MyActivities.html', context)
