from django.db import models


class Videocard(models.Model):
    PROMO_TYPES_CHOICES = [
        ('n', 'new'),
        ('r', 'regular'),
    ]
    name = models.CharField(max_length=50, verbose_name='Название')
    manufacturer = models.CharField(max_length=20, verbose_name='Производитель')
    price = models.IntegerField(null=True, verbose_name='цена')
    vendor = models.CharField(max_length=50, blank=True, verbose_name='Вендор')
    promo_type = models.CharField(max_length=10, choices=PROMO_TYPES_CHOICES, default='r')
    promo_note = models.CharField(max_length=300, blank=True, verbose_name='Промо-текст')
    image = models.FilePathField(path='media/', verbose_name='Изображение', blank=True)
    image_big = models.FilePathField(path='media/', verbose_name='Изображение большое', blank=True)
    background = models.FilePathField(path='media/', verbose_name='Фон', blank=True)


    def __str__(self):
        return str(self.name)