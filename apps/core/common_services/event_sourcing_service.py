import hashlib
from apps.core.models import Event


class EventSourcingService:
    """
    Сервис для работы с событиями (ивентами) в системе Event Sourcing.
    Позволяет создавать события, восстанавливать состояние агрегатов
    и предоставлять историю событий.
    """

    def record_event(self, user_id, event_type, payload: dict, target_id=None, client_id=None):
        """
        Создаёт новое событие на основе user_id и сохраняет его в базе данных.

        Args:
            user_id (int): Идентификатор пользователя, для которого создаётся событие.
            event_type (str): Тип события (например, 'created', 'updated').
            payload (dict): Данные, связанные с событием (изменённые или новые значения).
            target_id (int): Идентификатор пользователя или клиента, которого изменяют, если это не сам пользвоатель
            client_id (int): Идентификатор клиента.
        Returns:
            None
        """
        if target_id:
            aggregate_reference = ('target_id', target_id)
        elif client_id:
            aggregate_reference = ('client_id', client_id)
        else:
            aggregate_reference = ('user_id', user_id)

        prefix, reference_id = aggregate_reference
        aggregate_id = self.generate_aggregate_id(f'{prefix}_{reference_id}')

        if len(payload.keys()) > 1 or []:
            Event.objects.create(
                aggregate_id=aggregate_id,
                event_type=event_type,
                payload=payload,
                id_user_changing=user_id
            )

    @staticmethod
    def compare_fields_forms(forms: [], user_instance):
        """
        Сравнивает старые и новые значения полей форм с использованием changed_data.

        Args:
            forms (list): Список форм для сравнения.
            user_instance: Экземпляр пользователя, к которому привязаны формы.

        Returns:
            tuple: Словари старых и новых значений для изменённых полей.
        """
        old_values = {}
        new_values = {}

        for form in forms:
            if form.is_valid():
                form_instance = form.instance  # Экземпляр объекта формы
                model_instance = form_instance.__class__.objects.get(
                    pk=form_instance.pk)  # Получаем исходный объект из базы данных

                for field in form.changed_data:
                    # Получаем старое значение из исходного объекта
                    old_value = getattr(model_instance, field, None)

                    # Новое значение из очищенных данных формы
                    new_value = form.cleaned_data.get(field, None)

                    old_values[field] = old_value
                    new_values[field] = new_value

        return old_values, new_values

    @staticmethod
    def field_entry_to_payload(old_values, new_values, payload):
        """
        Записывает изменения в payload.

        Args:
            old_values (dict): Словарь старых значений.
            new_values (dict): Словарь новых значений.
            payload (dict): Существующий payload для записи.

        Returns:
            dict: Обновленный payload с изменениями.
        """
        for field in new_values:
            payload[field] = {'old': old_values.get(field), 'new': new_values[field]}
        return payload

    @staticmethod
    def generate_aggregate_id(user_id: str):
        """
        Генерирует уникальный идентификатор агрегата на основе идентификатора пользователя.

        Args:
            user_id (int): Идентификатор пользователя.

        Returns:
            str: Уникальный хешированный идентификатор агрегата.
        """
        return hashlib.sha256(f"user_{user_id}".encode()).hexdigest()

    @staticmethod
    def get_event_history(aggregate_id):
        """
        Возвращает список всех событий для заданного агрегата.

        Args:
            aggregate_id (str): Идентификатор агрегата, для которого требуется получить историю событий.

        Returns:
            QuerySet: Список событий, отсортированных по времени.
        """
        events = Event.objects.filter(aggregate_id=aggregate_id).order_by('timestamp')
        return events
