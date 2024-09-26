# from django.apps import apps
# from django.core.cache import cache
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
#
#
# # Универсальная функция для очистки кэша
# @receiver(post_save)
# @receiver(post_delete)
# def clear_cache(sender, **kwargs):
#     # Очистка кэша
#     cache.clear()
#
#
# # Функция для подключения сигнала ко всем моделям
# def connect_signals():
#     for model in apps.get_models():
#         post_save.connect(clear_cache, sender=model)
#         post_delete.connect(clear_cache, sender=model)
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import UserProfile


@receiver(m2m_changed, sender=UserProfile.dealership_manager.through)
def reset_active_dealership(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.active_dealership = None
        instance.save()

