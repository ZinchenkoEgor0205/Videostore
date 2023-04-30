from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Discount(models.Model):
    status_name = models.CharField(max_length=10, verbose_name=_('Название'))
    required_sum = models.IntegerField(default=0, verbose_name=_('Требуемая сумма'))
    price_multiplier = models.DecimalField(max_digits=3, decimal_places=2, verbose_name=_('Множитель цены'))

    def __str__(self):
        return self.status_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    city = models.CharField(max_length=30, blank=True, verbose_name=_('Город'))
    street = models.CharField(max_length=30, blank=True, verbose_name=_('Улица'))
    housing = models.CharField(max_length=10, blank=True, verbose_name=_('Корпус'))
    house = models.IntegerField(blank=True, null=True, verbose_name=_('Дом'))
    apartment = models.IntegerField(blank=True, null=True, verbose_name=_('Квартира'))
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, verbose_name=_('Скидка'))
    phone = models.CharField(max_length=15, blank=True, verbose_name=_('Телефон'))
    verification = models.BooleanField(default=False, verbose_name=_('Верификация'))
    total_sum = models.IntegerField(default=0, verbose_name=_('Общая сумма'))

    class Meta:
        verbose_name = 'profile'
        permissions = (
            ('can_verificate', 'Может верифицировать'),
        )

    def __str__(self):
        return self.user.username


