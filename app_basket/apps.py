from django.apps import AppConfig


class AppBasketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_basket'

    def ready(self):
        import app_main.views
        import app_basket.signals
