from django.apps import AppConfig


class QuestionnaireConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.questionnaire'

    def ready(self):
        pass
        # from apps.questionnaire.tasks import run_kafka_consumer
        # run_kafka_consumer.delay()

        # from apps.questionnaire.tasks import logout_all_users
        # logout_all_users.delay()