from django.test import TestCase
from ..models import Registro

class RegistroTestCase(TestCase):
    def test_registro(self):
        registro = Registro(nome='Elder', email='marquinhos@gmail.com')
        registro.save()

        registro_recuperado = Registro.objects.get(nome='Elder', email='marquinhos@gmail.com')

        self.assertEqual(registro_recuperado.nome, 'Elder')
        self.assertEqual(registro_recuperado.email, 'marquinhos@gmail.com')
