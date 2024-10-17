import uuid

from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aggregate_id = models.CharField(max_length=64)
    event_type = models.CharField(max_length=255)
    payload = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    id_user_changing = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.event_type} - {self.aggregate_id}"

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}'
