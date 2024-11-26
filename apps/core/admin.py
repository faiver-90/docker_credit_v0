from django.contrib import admin

from apps.core.models import Event, ResponseCalculationSovComBank


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'aggregate_id', 'event_type', 'payload', 'timestamp')
    search_fields = ('event_id', 'aggregate_id', 'event_type', 'payload', 'timestamp')


@admin.register(ResponseCalculationSovComBank)
class ResponseCalculationSovComBankAdmin(admin.ModelAdmin):
    list_display = ('request_id_in_bank', 'dealer_id')
    search_fields = ('request_id_in_bank', 'dealer_id')
