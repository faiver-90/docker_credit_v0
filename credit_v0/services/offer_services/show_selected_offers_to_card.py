from django.http import Http404
from django.shortcuts import get_object_or_404

from credit_v0.models import SelectedClientOffer, Offers


class ShowOfferService:
    """Сервис для работы с выбранными оферами"""

    @staticmethod
    def get_offer_data(offer_id: int, request) -> dict:
        """Получение и подготовка данных для офера"""

        # Получаем офер и проверяем, существует ли выбранное предложение
        offer = get_object_or_404(Offers, id=offer_id)
        select_offer = SelectedClientOffer.objects.filter(offer_id=offer_id).first()

        if not select_offer:
            raise Http404("SelectedClientOffer does not exist")

        # Получаем значения из GET-параметров или используем значения из select_offer
        offer.car_price_display_select = request.GET.get('car_price', select_offer.car_price_display_select)
        offer.initial_payment_select = request.GET.get('initial_payment', select_offer.initial_payment_select)
        offer.total_loan_amount_select = request.GET.get('total_loan_amount', select_offer.total_loan_amount_select)

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
