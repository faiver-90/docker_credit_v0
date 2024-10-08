class UserEditService:
    """
    Сервис для обработки изменений данных пользователя.
    """

    @staticmethod
    def add_dealership_to_payload(user_instance, profile_form, payload):
        """
        Добавляет изменения в поле 'dealership_manager' (ManyToMany) в payload, если они произошли.

        Args:
            user_instance: Экземпляр пользователя (User), чей профиль редактируется.
            profile_form: Форма профиля пользователя (ProfileEditForm), содержащая новые данные.
            payload: Словарь, в который будут записаны изменения.

        Returns:
            dict: Обновленный payload с изменениями в поле 'dealership_manager', если таковые произошли.
        """
        old_dealership = list(user_instance.userprofile.dealership_manager.all())
        if old_dealership is not None:
            new_dealership = list(profile_form.cleaned_data.get('dealership_manager', []))
            if set(old_dealership) != set(new_dealership):
                payload['dealership_manager'] = {
                    'old': [d.name for d in old_dealership],
                    'new': [d.name for d in new_dealership]
                }
        return payload
