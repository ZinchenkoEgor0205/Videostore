from django.contrib import admin

from app_basket.models import Order


@admin.register(Order)
class VideocardAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'phone', 'email', 'city', 'street', 'house', 'housing', 'apartment']
    list_filter = ['name_surname']