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
