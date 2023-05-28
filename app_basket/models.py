from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from app_main.models import Videocard


class Order(models.Model):
    name_surname = models.CharField(max_length=50, verbose_name=_('Имя и фамилия'))
    phone = models.CharField(max_length=20, verbose_name=_('Телефон'))
    email = models.EmailField(verbose_name=_('Электронная почта'))
    city = models.CharField(max_length=20, verbose_name=_('Город'))
    street = models.CharField(max_length=20, verbose_name=_('Улица'))
    house = models.CharField(max_length=10, verbose_name=_('Дом'))
    housing = models.IntegerField(verbose_name=_('Корпус'))
    apartment = models.IntegerField(verbose_name=_('Квартира'))
    sum = models.IntegerField(default=0, verbose_name=_('Сумма'))
    date = models.DateField(auto_now=False, auto_now_add=timezone.now().date(), verbose_name=_('Дата'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    videocards = models.ManyToManyField(Videocard, through='OrderVideocard', verbose_name=_('Видеокарты'))
    def __str__(self):
        return self.name_surname



class OrderVideocard(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('Заказ'))
    videocard = models.ForeignKey(Videocard, on_delete=models.CASCADE, verbose_name=_('Видеокарта'))
    quantity = models.IntegerField(default=1, verbose_name=_('Количество'))
