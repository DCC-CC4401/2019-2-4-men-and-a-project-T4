from django.contrib.auth.models import User
from django.test import TestCase, Client
import json

# Create your tests here.
from django.urls import reverse

from timePlan.models import *
import datetime


class PerfilUsuarioTestCase(TestCase):

    def setUp(self):
        global p, c
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        PerfilUsuario.objects.create(usuario=self.user, nombre="test", correo='test@mail.cl')

        p = PerfilUsuario.objects.get(nombre="test")
        c = Categoria.objects.create(c_nombre="test")

        Actividades.objects.create(
            user_id=p,
            nombre='test',
            descripcion='test',
            h_inicio=datetime.datetime(year=2019, month=11, day=2, hour=16, minute=0, second=0),
            duracion=datetime.time(hour=2, minute=0, second=0),
            categoria=c
        )

        Actividades.objects.create(
            user_id=p,
            nombre='test',
            descripcion='test',
            h_inicio=datetime.datetime(year=2019, month=11, day=5, hour=16, minute=0, second=0),
            duracion=datetime.time(hour=2, minute=0, second=0),
            categoria=c
        )

        Actividades.objects.create(
            user_id=p,
            nombre='test',
            descripcion='test',
            h_inicio=datetime.datetime(year=2019, month=11, day=10, hour=16, minute=0, second=0),
            duracion=datetime.time(hour=2, minute=0, second=0),
            categoria=c
        )

    def test_extraerActividadesSemanales(self):
        igualdad = Actividades.objects.get(
            h_inicio=datetime.datetime(year=2019, month=11, day=5, hour=16, minute=0, second=0))
        expected = p.extraerActividadesSemanales(datetime.date(year=2019, month=11, day=3))

        self.assertTrue(expected.count(), 1)
        set_de_datos = expected[0]

        self.assertEquals(igualdad.user_id, set_de_datos.user_id)
        self.assertEquals(igualdad.nombre, set_de_datos.nombre)
        self.assertEquals(igualdad.descripcion, set_de_datos.descripcion)
        self.assertEquals(igualdad.h_inicio, set_de_datos.h_inicio)
        self.assertEquals(igualdad.duracion, set_de_datos.duracion)
        self.assertEquals(igualdad.categoria.c_nombre, set_de_datos.categoria.c_nombre)

    def test_extraerEstadisticasSemanales(self):
        Actividades.objects.create(
            user_id=p,
            nombre='test',
            descripcion='test',
            h_inicio=datetime.datetime(year=2019, month=11, day=6, hour=16, minute=0, second=0),
            duracion=datetime.time(hour=2, minute=0, second=0),
            categoria=c
        )

        Actividades.objects.create(
            user_id=p,
            nombre='test',
            descripcion='test',
            h_inicio=datetime.datetime(year=2019, month=11, day=6, hour=18, minute=0, second=0),
            duracion=datetime.time(hour=1, minute=0, second=0),
            categoria=Categoria.objects.create(c_nombre="test2")
        )
        expected = {'test': 14400, 'test2': 3600}

        data = p.extraerEstadisticasSemanales(datetime.date(year=2019, month=11, day=3))
        for key in data:
            self.assertEquals(data[key].seconds, expected[key])


class timePlanViewsTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='username')
        self.user.set_password('secret')
        self.user.save()
        self.perfil = PerfilUsuario.objects.create(usuario=self.user, nombre="test", correo='test@mail.cl')

    def test_login(self):
        response = self.c.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'timePlan/login.html')

    def test_auth(self):
        response = self.client.post(reverse('auth'), {'correo': 'test@mail.cl', 'contrasena': 'failed'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timePlan/login.html')
        self.assertTrue(not response.context['user'].is_active)

        response = self.client.post(reverse('auth'), {'correo': 'test@mail.cl', 'contrasena': 'secret'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timePlan/LandingPage.html')
        self.assertTrue(response.context['user'].is_active)

    def test_landing(self):
        c = Categoria.objects.create(c_nombre="test")

        a = Actividades.objects.create(
            user_id=self.perfil,
            nombre='test',
            descripcion='test',
            h_inicio=datetime.datetime.now(),
            duracion=datetime.time(hour=2, minute=0, second=0),
            categoria=c
        )
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='username', password='secret')
        response = self.client.get(reverse('landing_page'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timePlan/LandingPage.html')
        self.assertEqual(response.context['username'], 'test')
        self.assertEqual(response.context['email'], 'test@mail.cl')
        self.assertEqual(response.context['photo'], 'fotos/aceitunas.jpg')

        categories = response.context['categories']
        expected = list(Categoria.objects.all().values())

        self.assertEqual(categories, expected)
