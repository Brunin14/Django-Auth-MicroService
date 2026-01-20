from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginTests(APITestCase):
    def setUp(self):
        self.login_url = reverse('users:jwt_login')
        self.email = "logar@teste.com"
        self.password = "Senha123!"
        self.user = User.objects.create_user(email=self.email, password=self.password)

    def test_login_success(self):
        """Deve retornar Tokens (Access/Refresh) ao logar"""
        data = {
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_invalid_credentials(self):
        """Deve negar login com senha errada"""
        data = {
            "email": self.email,
            "password": "SenhaErrada"
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)