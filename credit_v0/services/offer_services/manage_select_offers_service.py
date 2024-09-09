from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.loader import render_to_string

from credit_v0.models import SelectedClientOffer, ClientPreData, Offers, ClientCarInfo, ClientFinancingCondition


class SelectedOfferService:
    """Сервис для работы с CRUD-операциями для выбранных оферов."""

    @staticmethod
    def get_offers(client_id: int) -> list:
        """Получить список выбранных оферов для клиента."""
        client = get_object_or_404(ClientPreData, id=client_id)
        selected_offers = get_list_or_404(SelectedClientOffer, client=client)

        offers_data = [SelectedOfferService.render_offer(offer, client_id) for offer in selected_offers]
        return offers_data

    @staticmethod
    def render_offer(offer, client_id: int) -> str:
        """Рендеринг карточки офера."""
        context = {
            'offer': offer,
            'client_id': client_id,
            'hide_controls': False  # Удаление или показ кнопок выбрать, удалить на странице запросов
        }
        return render_to_string('questionnaire/card_offer.html', context)

    @staticmethod
    def create_or_update_offer(client_id: int, offer_id: int, total_loan_amount: float) -> dict:
        """Создание или обновление офера."""
        client = get_object_or_404(ClientPreData, id=client_id)
        offer_details = get_object_or_404(Offers, id=offer_id)
        car_info = get_object_or_404(ClientCarInfo, client=client)
        financing_conditions = get_object_or_404(ClientFinancingCondition, client=client)

        select_offer, created = SelectedClientOffer.objects.update_or_create(
            client=client,
            offer_id=offer_id,
            defaults={
                'car_price_display_select': car_info.car_price_car_info,
                'initial_payment_select': financing_conditions.initial_payment,
                'total_loan_amount_select': total_loan_amount,
                'title_select': offer_details.title,
                'term_select': offer_details.term,
                'monthly_payment_select': offer_details.pay,
                'stavka_select': offer_details.stavka,
                'name_bank_select': offer_details.name_bank
            }
        )

        if created:
            select_offer.id_app_in_system = select_offer.id
            select_offer.save()

        return {'status': 'success', 'created': created}

    @staticmethod
    def delete_offer(client_id: int, offer_id: int) -> dict:
        """Удаление выбранного офера."""
        client = get_object_or_404(ClientPreData, id=client_id)
        deleted = get_object_or_404(SelectedClientOffer, client=client, offer_id=offer_id).delete()

        if deleted:
            return {'status': 'success'}
        else:
            return {'status': 'error', 'message': 'Offer not found'}
