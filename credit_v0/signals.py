from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import UserProfile


@receiver(m2m_changed, sender=UserProfile.dealership_manager.through)
def reset_active_dealership(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.active_dealership = None
        instance.save()

