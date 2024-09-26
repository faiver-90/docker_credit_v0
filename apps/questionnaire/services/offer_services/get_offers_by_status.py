from typing import List, Dict

from django.shortcuts import get_list_or_404
from django.template.loader import render_to_string

from apps.questionnaire.models import SelectedClientOffer
from apps.questionnaire.services.constants import OFFER_STATUSES


class GetByStatusOfferService:
    """
    Сервис для получения оферов у которых есть статус и распределяет по группам
    """

    def __init__(self):
        # Инициализируем offers_data на основе статусов из константы
        self.offers_data = {status: [] for status in OFFER_STATUSES}

    def get_offers_by_status(self, client_id) -> Dict[str, list]:
        offers = get_list_or_404(SelectedClientOffer, client_id=client_id)

        for offer in offers:
            status = offer.status_select_offer
            if status and status in OFFER_STATUSES:  # Проверяем наличие статуса в константе
                offer_data = render_to_string('questionnaire/card_offer.html', {
                    'offer': offer,
                    'client_id': client_id,
                    'hide_controls': True
                })
                self.offers_data[status].append(offer_data)
        return self.offers_data
