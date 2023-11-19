from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse(viewname='programas-list')
        self.user = User.objects.create_user('C3-PO', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste para verifica a autenticacao de um user com as credenciais corretas"""
        user = authenticate(username='C3-PO', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica GET nao autorizada"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_user_com_username_incorreto(self):
        """Teste de autenticacao de usuario incorreto"""
        user = authenticate(username='C3-P1', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_user_com_password_incorreto(self):
        """Teste de autenticacao de senha incorreta"""
        user = authenticate(username='C3-PO', password='123457')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_com_user_autorizado(self):
        """Teste que verifica GET de user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        




