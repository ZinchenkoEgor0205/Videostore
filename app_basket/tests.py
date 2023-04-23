from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_main.models import Videocard, VideocardInfo
from app_user.models import Profile
from videostore_project import settings


class BasketDetailViewTestCase(TestCase):

    def setUp(self) -> None:
        self.credentials = {
            'username': 'test99',
            'password': 'test99'
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_basket_detail_view_without_login(self):
        response = self.client.get(reverse('basket_detail_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_basket_detail_view(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('basket_detail_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket_detail.html')


class BasketAddViewTestCase(TestCase):
    fixtures = ['database-fixtures.json']

    def setUp(self) -> None:
        self.credentials = {
            'username': 'test99',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)
        self.profile = Profile.objects.create(user=self.user, discount_id=3)
        self.videocard_info = VideocardInfo.objects.create(name='test videocard info')
        self.videocard = Videocard.objects.create(name='test videocard', price=547, info=self.videocard_info)

    def tearDown(self) -> None:
        self.user.delete()
        self.videocard.delete()

    def test_basket_add_view_without_login(self):
        response = self.client.post(reverse('basket_add_view', kwargs={'videocard_id': self.videocard.pk}),
                                    {'quantity': 4, 'update': True}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')

    def test_basket_add_view(self):
        self.client.login(**self.credentials)
        quantity = 6
        response = self.client.post(reverse('basket_add_view', kwargs={'videocard_id': self.videocard.pk}),
                                    {'quantity': quantity, 'update': True}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket_detail.html')
        basket = self.client.session.get(settings.BASKET_SESSION_ID)
        self.assertTrue(basket)
        self.assertTrue(basket[str(self.videocard.id)])
        self.assertTrue(
            basket[str(self.videocard.id)]['quantity'] == quantity and basket[str(self.videocard.id)]['price'] == str(
                self.videocard.price))


class BasketRemoveViewTestCase(TestCase):
    fixtures = ['database-fixtures.json']

    def setUp(self) -> None:
        self.credentials = {
            'username': 'test99',
            'password': 'test'}
        self.user = User.objects.create_user(**self.credentials)
        self.profile = Profile.objects.create(user=self.user, discount_id=3)
        self.videocard_info = VideocardInfo.objects.create(name='test videocard info')
        self.videocard = Videocard.objects.create(name='test videocard', price=547, info=self.videocard_info)

    def tearDown(self) -> None:
        self.user.delete()
        self.videocard.delete()

    def test_basket_remove_view_withot_login(self):
        response = self.client.get(reverse('basket_remove_view', kwargs={'videocard_id': self.videocard.id}),
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_basket_remove_view(self):
        self.client.login(**self.credentials)
        quantity = 6
        self.client.post(reverse('basket_add_view', kwargs={'videocard_id': self.videocard.pk}),
                         {'quantity': quantity, 'update': True}, follow=True)
        response = self.client.get(reverse('basket_remove_view', kwargs={'videocard_id': self.videocard.id}),
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket_detail.html')
        basket = self.client.session.get(settings.BASKET_SESSION_ID)
        self.assertFalse(basket)


class OrderViewTestCase(TestCase):
    fixtures = ['database-fixtures.json']

    def setUp(self) -> None:
        self.credentials = {
            'username': 'test99',
            'password': 'test'}
        self.user = User.objects.create_user(first_name='test', last_name='test', email='test@gmail.com',
                                             **self.credentials)
        self.profile = Profile.objects.create(user=self.user, discount_id=3, city='test_city', phone='88005553535',
                                              street='test_street', house=7, housing='6', apartment='8')
        self.videocard_info = VideocardInfo.objects.create(name='test videocard info')
        self.videocard = Videocard.objects.create(name='test videocard', price=547, info=self.videocard_info)

    def tearDown(self) -> None:
        self.user.delete()
        self.videocard.delete()

    def test_order_view_without_login(self):
        response = self.client.get(reverse('order_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_order_view_empty_basket(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('order_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_order_view(self):
        self.client.login(**self.credentials)
        quantity = 6
        self.client.post(reverse('basket_add_view', kwargs={'videocard_id': self.videocard.pk}),
                         {'quantity': quantity, 'update': True}, follow=True)
        response = self.client.get(reverse('order_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order.html')

    def test_order_view_post_wrong_form(self):
        self.client.login(**self.credentials)
        quantity = 6
        self.client.post(reverse('basket_add_view', kwargs={'videocard_id': self.videocard.pk}),
                         {'quantity': quantity, 'update': True}, follow=True)
        response = self.client.post(reverse('order_view'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket_detail.html')

    def test_order_view_post(self):
        self.client.login(**self.credentials)
        quantity = 6
        self.client.post(reverse('basket_add_view', kwargs={'videocard_id': self.videocard.pk}),
                         {'quantity': quantity, 'update': True}, follow=True)
        response = self.client.post(reverse('order_view'),
                                    {'name_surname': f'{self.user.first_name} {self.user.last_name}',
                                     'phone': self.user.profile.phone, 'email': self.user.email,
                                     'city': self.user.profile.city, 'street': self.user.profile.street,
                                     'house': self.user.profile.house, 'housing': self.user.profile.housing,
                                     'apartment': self.user.profile.apartment}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gratitude.html')
