import hashlib
from apps.core.models import Event


class EventSourcingService:
    """
    Сервис для работы с событиями (ивентами) в системе Event Sourcing.
    Позволяет создавать события, восстанавливать состояние агрегатов
    и предоставлять историю событий.
    """

    def record_event(self, user_id, event_type, payload, target_id=None, client_id=None):
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

        Event.objects.create(
            aggregate_id=aggregate_id,
            event_type=event_type,
            payload=payload,
            id_user_changing=user_id
        )

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

    # def get_aggregate_state(self, aggregate_id):
    #     """
    #     Восстанавливает текущее состояние агрегата (объекта) на основе всех событий.
    #
    #     Args:
    #         aggregate_id (str): Идентификатор агрегата, состояние которого нужно восстановить.
    #
    #     Returns:
    #         dict: Текущее состояние агрегата, построенное на основе последовательности событий.
    #     """
    #     events = Event.objects.filter(aggregate_id=aggregate_id).order_by('timestamp')
    #     state = {}
    #     for event in events:
    #         state = self.apply_event(state, event)
    #     return state
    #
    # @staticmethod
    # def apply_event(state, event):
    #     """
    #     Применяет событие к состоянию агрегата и обновляет его.
    #
    #     Args:
    #         state (dict): Текущее состояние агрегата.
    #         event (Event): Событие, которое нужно применить к состоянию.
    #
    #     Returns:
    #         dict: Обновлённое состояние агрегата.
    #     """
    #     if event.event_type == 'created':
    #         state.update(event.payload)
    #     elif event.event_type == 'updated':
    #         state.update(event.payload)
    #     elif event.event_type == 'deleted':
    #         # Обработка удаления - в зависимости от логики, можно удалять конкретные ключи
    #         for key in event.payload.keys():
    #             if key in state:
    #                 del state[key]
    #
    #     return state