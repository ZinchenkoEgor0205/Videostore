from django.contrib.auth.views import LogoutView
from django.urls import path

from app_main.views import *

urlpatterns = [
    path('', main_view, name='main_view'),
    path('<int:pk>/', VideocardDetailView.as_view(), name='videocard_detail')
]
