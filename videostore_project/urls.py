"""videostore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

import videostore_project.settings
from app_main.views import *
from app_user.views import login_view, register_view, account_view, logout_view
from videostore_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_view'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('test/', test_view, name='test'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=videostore_project.settings.MEDIA_ROOT)
