from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterTests(APITestCase):
    def setUp(self):
        # Dados padrão para testes
        self.register_url = reverse('users:custom_register') # O nome que demos no urls.py
        self.user_data = {
            "email": "novo@teste.com",
            "password": "SenhaForte123!",
            "password_confirm": "SenhaForte123!" # O dj-rest-auth pede confirmação às vezes
        }

    def test_register_success(self):
        """Deve criar uma conta com sucesso"""
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="novo@teste.com").exists())

    def test_register_duplicate_email(self):
        """Não deve permitir criar conta com e-mail já existente"""
        # Cria o primeiro
        User.objects.create_user(email="novo@teste.com", password="123")
        
        # Tenta criar o segundo igual
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)