from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    DISCOUNT_STATUS_CHOICES = [
        ('b', 'Bronze'),
        ('s', 'Silver'),
        ('g', 'Gold'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True)
    discount_status = models.CharField(max_length=1, choices=DISCOUNT_STATUS_CHOICES, default='b')
    phone = models.CharField(max_length=15, blank=True)
    verification = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'profile'
        permissions = (
            ('can_verificate', 'Может верифицировать'),
        )

    def __str__(self):
        return self.user.username