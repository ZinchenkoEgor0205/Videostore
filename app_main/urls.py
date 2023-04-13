from django.contrib.auth.views import LogoutView
from django.urls import path

from app_main.views import *

urlpatterns = [
    path('', main_view, name='main_view'),
    path('sorted/', videocards_sorted_view, name='videocard_sorted'),
    path(r'set-language/', set_language, name='set_language'),
    path('<int:pk>/', VideocardDetailView.as_view(), name='videocard_detail'),
    path('create/', VideocardCreateView.as_view(), name='videocard_create'),
    path('update/<int:pk>/', VideocardUpdateView.as_view(), name='videocard_update'),
    path('info_create/', VideocardInfoCreateView.as_view(), name='videocard_info_create'),
    path('api/videocards/', VideocardSerializedListView.as_view(), name='videocard_serialized_list'),
    path('api/videocards/<int:pk>/', VideocardSerializedDetailView.as_view(), name='videocard_serialized_detail')
]
