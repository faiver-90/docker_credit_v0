from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.loader import render_to_string

from credit_v0.models import ClientPreData, ClientOffer, Offers


class CreateUpdateOffersInDbService:
    """Сервис для работы с предложениями партнеров"""

    @staticmethod
    def get_client_offers(client_id: int) -> list:
        """Получение предложений для клиента"""
        client = get_object_or_404(ClientPreData, id=client_id)
        offers_client = get_list_or_404(ClientOffer, client=client)

        # Преобразуем предложения в HTML
        offers_data = [render_to_string('questionnaire/offer_item.html', {'offer': offer}) for offer in offers_client]
        return offers_data

    @staticmethod
    def create_client_offers(client_id: int, financing_term: int) -> list:
        """Создание новых предложений для клиента на основе условия финансирования"""
        offers = get_list_or_404(Offers, term=financing_term)
        client = get_object_or_404(ClientPreData, pk=client_id)

        # Удаляем старые предложения для клиента
        client_offers = get_list_or_404(ClientOffer, client=client)

        for _ in client_offers:
            _.delete()

        offers_data = []
        for offer in offers:
            created_offer = ClientOffer.objects.create(
                client=client,
                offer_id=offer.id,
                title_offer=offer.title,
                name_bank_offer=offer.name_bank,
                term_offer=offer.term,
                stavka_offer=offer.stavka,
                pay_offer=offer.pay
            )
            offers_data.append(created_offer)

        # Преобразуем предложения в HTML
        offers_html = [render_to_string('questionnaire/offer_item.html', {'offer': offer}) for offer in offers_data]
        return offers_html
