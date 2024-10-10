import json
import sys

from app_v0.settings import BASE_DIR
from apps.core.banking_services.sovcombank.sovcombank_services.banking_requests_service import BankingRequestsService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES, FIELD_RANGES, FIELD_ENUMS, REQUIRED_FIELDS


def validate_goods_list(data_request):
    """
    Функция проверяет, что в каждом элементе списка goods значение поля goodCost больше 0.0.
    Если поле goodCost равно 0, пустое или None, оно выводится с причиной ошибки.
    Если все поля корректны (больше 0.0), возвращается True.
    """
    goods_list = data_request.get('goods', [])

    # Если список товаров пуст, выводим причину ошибки и возвращаем False
    if not goods_list:
        print("Ошибка: Список товаров 'goods' отсутствует или пуст.")
        return False

    for index, good in enumerate(goods_list):
        good_cost = good.get('goodCost', None)

        # Если goodCost пуст, равен 0 или меньше, выводим причину ошибки
        if good_cost is None:
            print(f"Ошибка в товаре на позиции {index + 1}: Поле 'goodCost' отсутствует.")
            sys.exit(1)
        elif good_cost == 0.0:
            print(f"Ошибка в товаре на позиции {index + 1}: Поле 'goodCost' равно 0.")
            sys.exit(1)
        elif good_cost < 0.0:
            print(f"Ошибка в товаре на позиции {index + 1}: Поле 'goodCost' меньше 0.")
            sys.exit(1)

    # Если все проверки прошли успешно, возвращаем True
    return True


sovcombank_connect_api_service = BankingRequestsService(
    f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')

data = sovcombank_connect_api_service.template_data

application_info = {
    "applicationInfo": {
        "partnerId": "НАШ ДИЛЕРСКИЙ ЦЕНТР#г Москва#Москва#29276#Воронова Елена Юрьевна"
    }
}

source_system_info = {
    "sourceSystemInfo": {
        "idSystem": "Кредитная программа 1"
    }
}

credit_info = {
    "creditInfo": {
        "product": "Кредит на автомобиль",
        "period": "36",
        "limit": 974387.53
    }
}

person_info = {
    "person": {
        "firstName": "Павел",
        "lastName": "ТЕСТОВ",
        "sex": "m",
        "birthplace": "ИРКУТСКАЯ ОБЛ",
        "dob": "1990-01-01",
        "factAddressSameAsRegistration": True,
        "primaryDocument": {
            "docType": "Паспорт",
            "docNumber": "123456",
            "docSeries": "11 11",
            "issueOrg": "ЗАРЕЧНЫМ ОМ Г. ЙОШКАР-ОЛЫ",
            "issueDate": "2010-01-01",
            "issueCode": "123-002"
        },
        "registrationAddress": {
            "countryName": "Россия",
            "region": "gde to",
            "postCode": "123456"
        },
        "incomes": [{
            "incomeType": "",
            "incomeAmount": 0.0,
        }]
    }
}

goods = {
    "goods": [
        {
            "goodCost": 100.0},
        {
            "goodCost": 50.0
        }
    ]
}

data_request = sovcombank_connect_api_service.fill_templates_request(
    data,
    **goods,
    **application_info,
    **source_system_info,
    **credit_info,
    **person_info
)

if sovcombank_connect_api_service.validate_fields(data_request, REQUIRED_FIELDS, FIELD_TYPES, FIELD_RANGES,
                                                  FIELD_ENUMS) and validate_goods_list(data_request):
    print(json.dumps(data_request, indent=4, ensure_ascii=False))
