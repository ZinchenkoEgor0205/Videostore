from django.contrib.auth.models import User
from django.db import models

class Discount(models.Model):
    status_name = models.CharField(max_length=10)
    price_multiplier = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.status_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30, blank=True)
    housing = models.CharField(max_length=10, blank=True)
    house = models.IntegerField(blank=True, null=True)
    apartment = models.IntegerField(blank=True, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    verification = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'profile'
        permissions = (
            ('can_verificate', 'Может верифицировать'),
        )

    def __str__(self):
        return self.user.username


