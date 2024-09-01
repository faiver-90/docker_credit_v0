from django.template.loader import render_to_string

from credit_v0.models import SelectedClientOffer


class BankOfferService:
    @staticmethod
    def prepare_offer_data(client_id, offer_ids):
        """Готовит данные для отправки в Kafka"""

        return {
            'client_id': client_id,
            'selected_offers': offer_ids
        }

    @staticmethod
    def process_offers(client_id, offer_ids):
        """Обновляет статус предложений клиента на 'Одобрение'."""
        print('process_offers is start')
        for offer_id in offer_ids:
            offers = SelectedClientOffer.objects.filter(offer_id=offer_id, client_id=client_id)
            if offers.exists():
                for offer in offers:
                    offer.status_select_offer = 'Одобрение'
                    offer.save()
            else:
                print(f'Offer with id {offer_id} does not exist for client {client_id}')

    @staticmethod
    def check_if_saved(client_id, selected_offers):
        for offer_id in selected_offers:
            if not SelectedClientOffer.objects.filter(client_id=client_id,
                                                      offer_id=offer_id,
                                                      status_select_offer='Одобрение').exists():
                return False
        return True

    @staticmethod
    def get_offers_by_status(client_id):
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
