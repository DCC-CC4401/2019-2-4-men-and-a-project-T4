from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from timePlan.models import PerfilUsuario


class PerfilUsuarioTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        login = user.client.login(username='testuser', password='12345')
        PerfilUsuario.objects.create(usuario=user, nombre="test", correo='test@mail.cl')
        PerfilUsuario.objects.create(name="cat", sound="meow")
