from django.test import TestCase
from django.urls import reverse

class ViewsTestCase(TestCase):

    def test_inicio(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inicio.html')
    
    def test_cadastro(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_contato(self):
        response = self.client.get(reverse('contato'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contato.html')

    def test_noticia(self):
        response = self.client.get(reverse('noticia'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noticia.html')

    def test_termo(self):
        response = self.client.get(reverse('termo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'termo.html')

    def test_cancelar(self):
        response = self.client.get(reverse('cancelar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelar.html')
    
    
    
