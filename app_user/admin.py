from django.contrib import admin
from app_user.models import *

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'required_sum', 'price_multiplier']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone', 'street', 'housing', 'house', 'apartment', 'verification', 'total_sum',]
    list_filter = ['user']
