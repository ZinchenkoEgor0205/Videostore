from django.contrib import admin
from app_main.models import Videocard
from app_user.models import Profile


@admin.register(Videocard)
class VideocardAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'price', 'vendor', 'image', 'background', 'image_big', 'promo_type', 'promo_note']
    list_filter = ['price']
    # inlines = [ReplyInLine]

    # actions = ['mark_as_active', 'mark_as_nonactive']

    # def mark_as_active(self, request, queryset):
    #     queryset.update(status='a')
    #
    # def mark_as_nonactive(self, request, queryset):
    #     queryset.update(status='n')
    #
    # mark_as_active.short_description = 'Перевести в активные'
    # mark_as_nonactive.short_description = 'Перевести в неактивные'

@admin.register(Profile)
class VideocardAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'discount_status', 'phone', 'verification',]
    list_filter = ['user']