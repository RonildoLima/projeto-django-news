from django.test import TestCase
from django.urls import reverse
from ..models import Registro

class CancelarTestCase(TestCase):
    def setUp(self):
        self.registro = Registro.objects.create(nome='Elder', email='marquinhos@gmail.com')

    def test_cancelar_registro(self):
        response = self.client.post(reverse('cancelar'), {'email': 'marquinhos@gmail.com'})

        self.assertEqual(response.status_code, 200)

        with self.assertRaises(Registro.DoesNotExist):
            Registro.objects.get(email='marquinhos@gmail.com')
