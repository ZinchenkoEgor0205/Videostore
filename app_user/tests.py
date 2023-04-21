from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from app_user.models import Profile


class LoginViewTestCase(TestCase):

    def setUp(self) -> None:
        self.credentials = {
            'username': 'test',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)

    def tearDown(self) -> None:
        self.user.delete()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {'username': self.user.username, 'password': self.user.password})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class RegisterViewTestCase(TestCase):
    fixtures = ['app_user_discount-fixtures.json']

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post(self):
        response = self.client.post(reverse('register'), {'username': 'test', 'first_name': 'test', 'last_name': 'test',
                                                          'email': 'test@gmail.com', 'phone': 88005553535,
                                                          'city': 'city', 'password1': 'try8800555',
                                                          'password2': 'try8800555'})
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='test')
        self.assertTrue(user)


class AccountViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.credentials = {
            'username': 'test',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)

    def test_account_view_without_login(self):
        response = self.client.get(reverse('account'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_account_view(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
