from apps.core.models import Notification


def recording_notification_message(user, message):
    Notification.objects.create(
        user=user,
        message=str(message),
        is_read=False
    )
