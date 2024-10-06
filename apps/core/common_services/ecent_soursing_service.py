import hashlib

from apps.core.models import Event


class EventSourcingService:
    @staticmethod
    def record_event(aggregate_id, event_type, payload):
        event = Event.objects.create(
            aggregate_id=aggregate_id,
            event_type=event_type,
            payload=payload
        )

        return event

    @staticmethod
    def get_aggregate_state(aggregate_id):
        events = Event.objects.filter(aggregate_id=aggregate_id).order_by('timestamp')
        state = {}
        for event in events:
            state = EventSourcingService.apply_event(state, event)

        return state

    @staticmethod
    def apply_event(state, event):
        if event.event_type == 'created':
            state.update(event.payload)
        elif event.event_type == 'updated':
            state.update(event.payload)

        return state

    @staticmethod
    def get_event_history(aggregate_id):
        events = Event.objects.filter(aggregate_id=aggregate_id).order_by('timestamp')

        return events

    @staticmethod
    def generate_aggregate_id(user_id):
        return hashlib.sha256(f"user_{user_id}".encode()).hexdigest()
