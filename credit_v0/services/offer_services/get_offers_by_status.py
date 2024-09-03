from typing import List, Dict

from django.template.loader import render_to_string

from credit_v0.models import SelectedClientOffer


class GetByStatusOfferService:
    """
    Сервис для получения оферов у которых есть статус и распределяет по группам
    """
    @staticmethod
    def get_offers_by_status(client_id) -> Dict[str, list]:
        offers = SelectedClientOffer.objects.filter(client_id=client_id)
        offers_data = {
            'Ошибка': [],
            'Ожидание решения': [],
            'Отказ': [],
            'Запрос доп информации': [],
            'Одобрение': []
        }
        for offer in offers:
            status = offer.status_select_offer
            if status:
                offer_data = render_to_string('questionnaire/card_offer.html', {
                    'offer': offer,
                    'client_id': client_id,
                    'hide_controls': True
                })
                offers_data[status].append(offer_data)
        return offers_data
