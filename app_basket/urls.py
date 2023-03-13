from django.urls import path

from app_basket.views import *

urlpatterns = [
    path('', basket_detail_view, name='basket_detail_view'),
    path('add/<int:videocard_id>/', basket_add_view, name='basket_add_view'),
    path('remove/<int:videocard_id>', basket_remove_view, name='basket_remove_view'),
    path('order', order_view, name='order_view'),
    path('gratitude', gratitude_view, name='gratitude_view'),
]
