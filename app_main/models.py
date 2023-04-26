from django.db import models
from django.utils.translation import gettext_lazy as _


def videocard_directory_path(instance: 'Videocard', filename: str) -> str:
    return f'videocards/{instance.name}/image/{filename}'


class VideocardInfo(models.Model):
    name = models.CharField(unique=True, max_length=50)
    release_date = models.IntegerField(blank=True, null=True)
    interface = models.CharField(max_length=50, blank=True)
    core_frequency = models.IntegerField(blank=True, null=True)
    core_count = models.IntegerField(blank=True, null=True)
    memory_frequency = models.IntegerField(blank=True, null=True)
    memory_type = models.CharField(max_length=20, blank=True)
    memory_volume = models.IntegerField(blank=True, null=True)
    memory_band_width = models.IntegerField(blank=True, null=True)
    recommended_energy_supply = models.IntegerField(blank=True, null=True)

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
    info = models.ForeignKey(VideocardInfo, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.name)
