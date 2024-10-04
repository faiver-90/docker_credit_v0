from django.db.models.signals import m2m_changed

from log_storage.logging_config import logger_error
from apps.users.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(m2m_changed, sender=UserProfile.dealership_manager.through)
def reset_active_dealership(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.active_dealership = None
        instance.save()


@receiver(post_save, sender=UserProfile)
def assign_group_on_profile_creation(sender, instance, created, **kwargs):
    if created:
        user_profile = instance
        group = None

        # Проверка и создание группы, если она не существует
        if user_profile.role_manager == 'admin':
            group, created_group = Group.objects.get_or_create(name='Admins')
        elif user_profile.role_manager == 'owner':
            group, created_group = Group.objects.get_or_create(name='Owners')
        elif user_profile.role_manager == 'Менеджер ДЦ':
            group, created_group = Group.objects.get_or_create(name='Managers')

        if group:
            user_profile.user.groups.add(group)
        else:
            logger_error(
                f'Пользователь {user_profile.user.username} имеет неизвестную роль: {user_profile.role_manager}')
