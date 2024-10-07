class UserEditService:
    """
    Сервис для обработки изменений данных пользователя и их сравнения с предыдущими значениями.
    """

    @staticmethod
    def save_old_feild(user_instance, profile_form):
        """
        Сохраняет старые значения полей профиля пользователя для последующего сравнения.

        Args:
            user_instance: Экземпляр пользователя (User), чей профиль редактируется.
            profile_form: Форма профиля пользователя (ProfileEditForm).

        Returns:
            Tuple: Словарь с предыдущими значениями полей профиля и список дилерских центров (ManyToManyField).
        """
        old_values = {
            field: getattr(user_instance.userprofile, field)
            for field in profile_form.fields
        }
        old_dealership = list(user_instance.userprofile.dealership_manager.all())
        return old_values, old_dealership

    @staticmethod
    def compare_fields(profile_form, old_values, payload, old_dealership):
        """
        Сравнивает новые данные профиля с предыдущими значениями и добавляет изменения в payload.

        Args:
            profile_form: Форма профиля пользователя (ProfileEditForm), содержащая новые данные.
            old_values: Словарь с предыдущими значениями полей профиля.
            payload: Словарь, в который будут записаны измененные поля.
            old_dealership: Список предыдущих значений для поля дилерского центра (ManyToManyField).

        Returns:
            payload: Словарь, дополненный изменёнными полями профиля.
        """
        for field in profile_form.changed_data:
            old_value = old_values.get(field)
            new_value = profile_form.cleaned_data[field]

            if old_value != new_value:
                payload[field] = {'old': old_value, 'new': new_value}

        new_dealership = list(profile_form.cleaned_data.get('dealership_manager'))

        if set(old_dealership) != set(new_dealership):
            payload['dealership_manager'] = {
                'old': [d.name for d in old_dealership],
                'new': [d.name for d in new_dealership]
            }

        return payload
