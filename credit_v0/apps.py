from django.apps import AppConfig


class CreditV0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'credit_v0'

    def ready(self):
        from .signals import reset_active_dealership
        reset_active_dealership

        from credit_v0.tasks import run_kafka_consumer
        run_kafka_consumer.delay()

        from credit_v0.tasks import logout_all_users
        logout_all_users.delay()
