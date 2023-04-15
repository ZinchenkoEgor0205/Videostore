from django.db.models import Max
from django.test import TestCase
from django.urls import reverse

from app_main.models import Videocard, VideocardInfo


class MainViewTestCase(TestCase):

    fixtures = ['app_main-fixtures.json',]


    def test_main_view(self):
        response = self.client.get(reverse('main_view'))
        self.assertEqual(response.status_code, 200)


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


    def test_videocard_detail_view_and_check_content(self):
        response = self.client.get(reverse('videocard_detail', kwargs={'pk': self.videocard.pk}))
        self.assertContains(response, self.videocard.name)