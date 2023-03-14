from django.contrib import admin
from app_user.models import *

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'price_multiplier']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone', 'verification',]
    list_filter = ['user']
