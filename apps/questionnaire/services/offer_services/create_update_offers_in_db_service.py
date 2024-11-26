import logging

from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.loader import render_to_string

from apps.core.models import ResponseCalculationSovComBank, CalculationSovComBank, CreditInfoSovComBank, \
    DealCostSovComBank, OffersSovComBank
from apps.questionnaire.models import ClientPreData, ClientOffer, Offers

logger = logging.getLogger(__name__)


class CreateUpdateOffersInDbService:
    """Сервис для работы с предложениями партнеров"""

    @staticmethod
    def get_client_offers(client_id: int) -> list:
        """Получение предложений для клиента"""
        # client = get_object_or_404(ClientPreData, id=client_id)
        # offers_client = get_list_or_404(ClientOffer, client=client)
        # request_from_db = get_list_or_404(ResponseCalculationSovComBank, client=client)
        # logger.info(offers_client)
        # offers = {}
        # # Преобразуем предложения в HTML
        # offers_data = [render_to_string('questionnaire/offer_item.html',
        #                                 {'offer': offer}) for offer in offers_client]
        # return offers_data
        """Получение предложений для клиента с необходимыми полями"""
        client = get_object_or_404(ClientPreData, id=client_id)

        response_calculations = ResponseCalculationSovComBank.objects.filter(client=client)

        offers_data = []

        for response in response_calculations:
            calculations = CalculationSovComBank.objects.filter(request=response)

            for calculation in calculations:
                try:
                    credit_info = CreditInfoSovComBank.objects.get(calculation=calculation)

                    # Получаем рейтинг продукта из модели OffersSovComBank
                    offer_sovcom = OffersSovComBank.objects.filter(id_in_excel_file_sovcom=credit_info.product).first()

                    if not offer_sovcom:
                        logger.warning(f"Не найден рейтинг для продукта: {credit_info.product}")
                        rating = 0  # Если не найдено, присваиваем минимальный рейтинг
                    else:
                        rating = offer_sovcom.rating_sovcom

                    deal_cost = DealCostSovComBank.objects.get(calculation=calculation)

                    offer_data = {
                        'isCalculationPositive': calculation.is_calculation_positive,
                        'name_bank_offer': 'СовКомБанк',
                        'rating': rating,

                        'creditInfo': {
                            'productName': credit_info.product_name,
                            'product': credit_info.product,
                            'period': credit_info.period,
                            'payment': credit_info.payment,
                            'paymentNoSubsidy': credit_info.payment_no_subsidy,
                            'creditAmount': credit_info.credit_amount,
                            'monthlyPayment': credit_info.monthly_payment,
                            'creditRate': credit_info.credit_rate,
                        },
                        'dealCost': {
                            'amount': deal_cost.amount
                        }
                    }
                    offers_data.append(offer_data)

                except (CreditInfoSovComBank.DoesNotExist, DealCostSovComBank.DoesNotExist) as e:
                    logger.error(f"Связанные данные отсутствуют для расчета: {calculation.id}. Ошибка: {str(e)}")

        # Сортировка предложений по рейтингу в убывающем порядке
        offers_data = sorted(offers_data, key=lambda x: x['rating'], reverse=True)

        # Преобразуем предложения в HTML
        offers_html = [render_to_string('questionnaire/offer_item.html', {'offer': offer}) for offer in offers_data]

        return offers_html

    @staticmethod
    def create_client_offers(client_id: int, financing_term: int) -> list:
        """Создание новых предложений для клиента на основе условия финансирования"""
        offers = get_list_or_404(Offers, term=financing_term)
        client = get_object_or_404(ClientPreData, pk=client_id)

        # Удаляем старые предложения для клиента
        ClientOffer.objects.filter(client=client).delete()
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
