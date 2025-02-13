from django.template.loader import render_to_string

from apps.questionnaire.models import SelectedClientOffer


class SendToBankService:
    @staticmethod
    def prepare_selected_offer_data(client_id, offer_ids):
        """Готовит данные для отправки в Kafka"""
        return {
            'client_id': client_id,
            'selected_offers': offer_ids
        }

    @staticmethod
    def process_offers(client_id, offer_ids, **kwargs):
        """Обновляет статус предложений клиента на 'Одобрение'."""
        for offer_id in offer_ids:
            offers = SelectedClientOffer.objects.filter(offer_id=offer_id, client_id=client_id, **kwargs)
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

    def send_to_bank_offers(self):
        pass
