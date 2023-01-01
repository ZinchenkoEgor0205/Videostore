from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from app_main.models import Videocard

def main_view(request):
    videocards = Videocard.objects.filter(promo_type='r')
    videocards_promo = Videocard.objects.filter(promo_type='n')
    user = request.user
    return render(request, 'main.html', context= {'videocards': videocards, 'videocards_promo': videocards_promo, 'user': user})

def test_view(request):
    return render(request, 'test.html')