from django.test import TestCase, Client
from django.contrib.staticfiles import finders

# Create your tests here.
from django.urls import reverse


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_userRegister(self):
        response = self.client.post(reverse('register_user'), {
            'usuario': 'test',
            'correoR': 'testing@test.cl',
            'contrasenaR': 'test',
            'cContrasena': 'test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('timePlan/LandingPage.html')

