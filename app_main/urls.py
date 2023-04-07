from django.contrib.auth.views import LogoutView
from django.urls import path

from app_main.views import *

urlpatterns = [
    path('', main_view, name='main_view'),
    path('sorted/', videocards_sorted_view, name='videocard_sorted'),
    path(r'set-language/', set_language, name='set_language'),
    path('<int:pk>/', VideocardDetailView.as_view(), name='videocard_detail'),
    path('api/videocards/', VideocardSerializedListView.as_view(), name='videocard_serialized_list'),
    path('api/videocards/<int:pk>/', VideocardSerializedDetailView.as_view(), name='videocard_serialized_detail')
]
