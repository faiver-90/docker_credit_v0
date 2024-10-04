from typing import Dict, List

from django.shortcuts import get_object_or_404

from apps.questionnaire.forms.car_application_form import CarInfoForm, DocumentAutoForm
from apps.questionnaire.models import ClientPreData, SelectedClientOffer


class ContinueDocsService:
    """
    Сервис для подготовки данных для страницы оформления заявки после одобрения.
    """

    @staticmethod
    def get_context_for_continue_fill(client_id, id_app_in_system) -> Dict[str, str]:
        """
        Получает необходимые данные и формирует контекст для рендеринга.
        """
        client = get_object_or_404(ClientPreData, id=client_id)
        offer = SelectedClientOffer.objects.filter(client=client, id_app_in_system=id_app_in_system).first()

        car_form = CarInfoForm(instance=client.car_info.first())
        document_form = DocumentAutoForm(instance=client.documents.first())

        context = {
            'client_id': client_id,
            'offer': offer,
            'id_app_in_system': id_app_in_system,
            'car_form': car_form,
            'document': document_form,
            'hide_all_button': True
        }
        return context
