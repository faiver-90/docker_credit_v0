from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CreditV0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credit_v0'

    def ready(self):
        from .signals import reset_active_dealership
        reset_active_dealership
