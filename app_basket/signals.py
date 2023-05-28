from django.dispatch import Signal, receiver

from app_basket.models import Order

order_saved = Signal()


@receiver(order_saved, sender=Order)
def handle_order_save(sender, request, **kwargs):
    print(request.session.get('success'))
    request.session['success'] = True
    request.session.save()
