
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from app_main.models import Videocard


class Order(models.Model):
    name_surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=10)
    housing = models.IntegerField()
    apartment = models.IntegerField()
    sum = models.IntegerField(default=0)
    date = models.DateField(auto_now=False, auto_now_add=timezone.now().date())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videocards = models.ManyToManyField(Videocard, through='OrderVideocard')

    def __str__(self):
        return self.name_surname


class OrderVideocard(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    videocard = models.ForeignKey(Videocard, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

