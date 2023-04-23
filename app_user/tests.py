from django.contrib.auth.models import User
from django.test import TestCase
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
        self.credentials = {
            'username': 'test',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)

    def tearDown(self) -> None:
        self.user.delete()

    def test_account_view_without_login(self):
        response = self.client.get(reverse('account'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_account_view(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')


class AccountEditViewTestCase(TestCase):

    fixtures = ['database-fixtures.json',]
    def setUp(self) -> None:
        self.credentials = {
            'username': 'test99',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)
        self.profile = Profile.objects.create(user=self.user, discount_id=3)

    def tearDown(self) -> None:
        self.user.delete()


    def test_account_edit_view_without_login(self):
        response = self.client.get(reverse('account_edit'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_account_edit_view(self):
        self.client.login(username='test99', password='test')
        response = self.client.get(reverse('account_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account-edit.html')

    def test_account_edit_view_post(self):
        self.client.login(username='test99', password='test')
        response = self.client.post(reverse('account_edit'), {'first_name': 'test777', 'house': 2, 'apartment': 20}, follow=True)
        user = User.objects.get(first_name='test777')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
        self.assertTrue(user)


class LogoutTestCase(TestCase):

    fixtures = ['database-fixtures.json']
    def setUp(self) -> None:
        self.credentials = {
            'username': 'test99',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)
        self.client.login(username='test99', password='test')

    def tearDown(self) -> None:
        self.user.delete()

    def test_logout(self):

        response = self.client.get(reverse('logout'), follow=True)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        # user = response.user
        # self.assertFalse(user.is_authenticated)



