from django.contrib import admin
from django.utils.safestring import mark_safe

from app_main.models import Videocard, VideocardInfo
from app_user.models import Profile


@admin.register(Videocard)
class VideocardAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'price', 'vendor', 'image_show', 'background', 'image_big', 'promo_type', 'promo_note']
    list_filter = ['price']
    list_editable = ['price', 'promo_type']

    def image_show(self, obj):
        if obj.image:
            return mark_safe(f'<img src="/{obj.image}" width="60" alt="image">')
        return 'None'

    image_show.__name__ = 'Картинка'

@admin.register(VideocardInfo)
class VideocardInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'release_date']


@admin.register(Profile)
class VideocardAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'discount_status', 'phone', 'verification',]
    list_filter = ['user']