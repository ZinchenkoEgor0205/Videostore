from django.contrib import admin

from app_basket.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name_surname', 'phone', 'email', 'city', 'street', 'house', 'housing', 'apartment', 'date']
    list_filter = ['name_surname']