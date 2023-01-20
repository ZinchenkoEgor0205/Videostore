from django.contrib.auth.views import LogoutView
from django.urls import path

from app_user.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
