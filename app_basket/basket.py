from decimal import Decimal

from django.http import request

from app_main.models import Videocard
from videostore_project import settings


class Basket(object):

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        videcards_ids = self.basket.keys()
        videocards = Videocard.objects.filter(id__in=videcards_ids)
        basket = self.basket.copy()
        for videocard in videocards:
            basket[str(videocard.id)]['videocard'] = videocard

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def add(self, videocard, quantity=1, update_quantity=False):

        videocard_id = str(videocard.id)
        if videocard_id not in self.basket:
            self.basket[videocard_id] = {'quantity': 0,
                                         'price': str(videocard.price)}
        if update_quantity:
            self.basket[videocard_id]['quantity'] = quantity
        else:
            self.basket[videocard_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, videocard):
        videocard_id = str(videocard.id)
        if videocard_id in self.basket:
            del self.basket[videocard_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.save()