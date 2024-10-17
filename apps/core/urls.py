from django.urls import path

from apps.questionnaire.views import get_notifications, mark_notification_as_read

urlpatterns = [
    path('get_notifications/', get_notifications, name='get_notifications'),
    path('mark_notification_as_read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
]
