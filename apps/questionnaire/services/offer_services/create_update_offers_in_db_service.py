import logging

from django.shortcuts import get_object_or_404, get_list_or_404
from django.template.loader import render_to_string

from apps.core.models import ResponseCalculationSovComBank, CalculationSovComBank, CreditInfoSovComBank, \
    DealCostSovComBank
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
        # 1. Получаем объект клиента
        client = get_object_or_404(ClientPreData, id=client_id)

        # 2. Получаем все расчеты для клиента из ResponseCalculationSovComBank
        response_calculations = ResponseCalculationSovComBank.objects.filter(client=client)

        offers_data = []

        # 3. Итерируем по каждому ResponseCalculationSovComBank и собираем данные
        for response in response_calculations:
            # Получаем все расчеты, связанные с данным запросом
            calculations = CalculationSovComBank.objects.filter(request=response)

            for calculation in calculations:
                try:
                    # Извлекаем связанные данные из CreditInfo и DealCost
                    credit_info = CreditInfoSovComBank.objects.get(calculation=calculation)
                    deal_cost = DealCostSovComBank.objects.get(calculation=calculation)

                    # Формируем нужные данные
                    offer_data = {
                        'isCalculationPositive': calculation.is_calculation_positive,
                        'name_bank_offer': 'СовКомБанк',
                        'creditInfo': {
                            'productName': credit_info.product_name,
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

                    # Рендеринг данных в HTML
                    offer_html = render_to_string('questionnaire/offer_item.html', {'offer': offer_data})
                    offers_data.append(offer_html)

                except (CreditInfoSovComBank.DoesNotExist, DealCostSovComBank.DoesNotExist) as e:
                    logger.error(f"Связанные данные отсутствуют для расчета: {calculation.id}. Ошибка: {str(e)}")

        return offers_data

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
