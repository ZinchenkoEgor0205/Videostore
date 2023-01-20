from django.urls import path

from app_basket.views import *

urlpatterns = [
    path('', basket_detail_view, name='basket_detail'),
    path('add/<int:videocard_id>/', basket_add_view, name='basket_add'),
    path('remove/<int:videocard_id>', basket_remove_view, name='basket_remove'),
]
