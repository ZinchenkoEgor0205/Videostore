from django.contrib.auth.views import LogoutView
from django.urls import path

from app_user.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/', AccountView.as_view(), name='account'),
    path('account_edit/', AccountEditView.as_view(), name='account_edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
