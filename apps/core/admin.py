from django.contrib import admin

from apps.core.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'aggregate_id', 'event_type', 'payload', 'timestamp')
    search_fields = ('event_id', 'aggregate_id', 'event_type', 'payload', 'timestamp')
