from django.db import models
from django.utils.translation import gettext_lazy as _


def videocard_directory_path(instance: 'Videocard', filename: str) -> str:
    return f'videocards/{instance.name}/image/{filename}'


class VideocardInfo(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name=_('Имя'))
    release_date = models.IntegerField(blank=True, null=True, verbose_name=_('Дата выхода'))
    interface = models.CharField(max_length=50, blank=True, verbose_name=_('Интерфейс'))
    core_frequency = models.IntegerField(blank=True, null=True, verbose_name=_('Частота ядра'))
    core_count = models.IntegerField(blank=True, null=True, verbose_name=_('Число ядер'))
    memory_frequency = models.IntegerField(blank=True, null=True, verbose_name=_('Частота памяти'))
    memory_type = models.CharField(max_length=20, blank=True, verbose_name=_('Тип памяти'))
    memory_volume = models.IntegerField(blank=True, null=True, verbose_name=_('Объём памяти'))
    memory_band_width = models.IntegerField(blank=True, null=True, verbose_name=_('Размер шины памяти'))
    recommended_energy_supply = models.IntegerField(blank=True, null=True, verbose_name=_('Рекомендованная мощность источника питания'))

    def __str__(self):
        return str(self.name)


class Videocard(models.Model):
    PROMO_TYPES_CHOICES = [
        ('n', 'new'),
        ('r', 'regular'),
    ]
    name = models.CharField(max_length=50, verbose_name=_('Название'))
    manufacturer = models.CharField(max_length=20, verbose_name=_('Производитель'))
    price = models.IntegerField(null=True, verbose_name=_('Цена'))
    vendor = models.CharField(max_length=50, blank=True, verbose_name=_('Вендор'))
    promo_type = models.CharField(max_length=10, choices=PROMO_TYPES_CHOICES, default='r')
    promo_note = models.CharField(max_length=300, blank=True, verbose_name=_('Промо-текст'))
    image = models.ImageField(upload_to=videocard_directory_path, verbose_name=_('Изображение'), blank=True, null=True)
    image_big = models.ImageField(upload_to=videocard_directory_path, verbose_name=_('Изображение большое'), blank=True, null=True)
    info = models.ForeignKey(VideocardInfo, on_delete=models.CASCADE, blank=True, verbose_name=_('Инфо'))

    def __str__(self):
        return str(self.name)
