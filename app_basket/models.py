from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    name_surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=10)
    housing = models.IntegerField()
    apartment = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
