from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse

from app_main.models import Videocard, VideocardInfo


class MainViewTestCase(TestCase):
    fixtures = ['app_main-fixtures.json', ]

    def test_main_view(self):
        response = self.client.get(reverse('main_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertQuerysetEqual(qs=Videocard.objects.all().order_by('id'),
                                 values=(v.pk for v in response.context['videocards']),
                                 transform=lambda v: v.pk)


class VideocardDetailViewTestCase(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.videocard_info = VideocardInfo.objects.create(name='test videocard info')
        cls.videocard = Videocard.objects.create(name='test videocard', info_id=cls.videocard_info.id)

    @classmethod
    def tearDown(cls) -> None:
        cls.videocard_info.delete()
        cls.videocard.delete()

    def test_videocard_detail_view(self):
        response = self.client.get(reverse('videocard_detail', kwargs={'pk': self.videocard.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'videocard_detail.html')

    def test_videocard_detail_view_and_check_content(self):
        response = self.client.get(reverse('videocard_detail', kwargs={'pk': self.videocard.pk}))
        self.assertContains(response, self.videocard.name)


class VideocardSortedViewTestCase(TestCase):

    def test_videocards_sorted_view(self):
        response = self.client.get(reverse('videocard_sorted'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'videocards_sorted.html')

class VideocardCreateViewTestCase(TestCase):

    fixtures = ['app_main-fixtures.json',]

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test1', password='test1')
        permission = Permission.objects.get(codename='add_videocard')
        self.user.user_permissions.add(permission)
        self.client.force_login(user=self.user)

    def tearDown(self):
        self.user.delete()

    def test_videocard_create_view(self):
        response = self.client.get(reverse('videocard_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'videocard_create.html')

    def test_videocard_create_view_post(self):
        response = self.client.post(reverse('videocard_create'), {'name': 'RTX 3060', 'manufacturer': 'Nvidia', 'price': 562, 'promo_type': 'r', 'info': 4}, follow=True)
        videocard = Videocard.objects.get(price=562, name='RTX 3060')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertTrue(videocard)


class VideocardUpdateViewTestCase(TestCase):
    fixtures = ['app_main-fixtures.json', ]

    def setUp(self) -> None:
        self.videocard = Videocard.objects.get(name='RTX 3060ti', vendor='MSI')
        self.user = User.objects.create_user(username='test1', password='test1')
        permission = Permission.objects.get(codename='change_videocard')
        self.user.user_permissions.add(permission)
        self.client.force_login(user=self.user)

    def tearDown(self):
        self.user.delete()

    def test_videocard_update_view(self):
        response = self.client.get(reverse('videocard_update', kwargs={'pk': self.videocard.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'videocard_update.html')

    def test_videocard_update_view_post(self):
        response = self.client.post(reverse('videocard_update', kwargs={'pk': self.videocard.pk}), {'name': 'RTX 3060ti', 'manufacturer': 'Nvidia', 'price': 200, 'promo_type': 'r', 'info': 8,})
        self.assertEqual(response.status_code, 302)

