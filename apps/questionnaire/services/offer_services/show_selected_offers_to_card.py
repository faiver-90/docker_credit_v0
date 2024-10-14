from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404

from apps.questionnaire.models import SelectedClientOffer, Offers


class ShowOfferService:
    """Сервис для работы с выбранными оферами"""

    @staticmethod
    def get_offer_data(offer_id: int, car_price=None, initial_payment=None, total_loan_amount=None) -> dict:
        """Получение и подготовка данных для офера"""

        # Получаем офер и проверяем, существует ли выбранное предложение
        offer = get_object_or_404(Offers, id=offer_id)
        select_offer = SelectedClientOffer.objects.filter(offer_id=offer_id).first()

        if not select_offer:
            raise Http404("SelectedClientOffer does not exist")

        # Используем переданные значения или значения из select_offer
        offer.car_price_display_select = car_price or select_offer.car_price_display_select
        offer.initial_payment_select = initial_payment or select_offer.initial_payment_select
        offer.total_loan_amount_select = total_loan_amount or select_offer.total_loan_amount_select

        offer.offer_id = offer_id
        offer.title_select = offer.title
        offer.name_bank_select = offer.name_bank
        offer.term_select = offer.term
        offer.stavka_select = offer.stavka
        offer.monthly_payment_select = offer.pay

        # Формируем контекст для передачи в шаблон
        context = {
            'offer': offer,
            'client_id': select_offer.client.id,
            'hide_controls': False  # Контролируем отображение кнопок
        }

        return context
