import json
import sys
from pathlib import Path

from apps.core.banking_services.sovcombank.sovcombank_services.banking_requests_service import BankingRequestsService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES, FIELD_RANGES, FIELD_ENUMS, REQUIRED_FIELDS

project_root = Path(__file__).resolve().parent.parent.parent


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
    f'{project_root}/templates_json/sovcombank_shot.json')

data = sovcombank_connect_api_service.template_data


filled_data = {
    "applicationInfo": {
        "partnerId": "НАШ ДИЛЕРСКИЙ ЦЕНТР#г Москва#Москва#29276#Воронова Елена Юрьевна"
    },
    "sourceSystemInfo": {
        "idSystem": "Кредитная программа 1"
    },
    "creditInfo": {
        "product": "Кредит на автомобиль",
        "period": "36",
        "limit": 974387.53
    },
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
        "incomes": [
            {
                "incomeType": "",
                "incomeSource": "",
                "incomeAmount": 0.0,
                "incomeFrequency": "",
                "incomeDay": "",
                "incomeDay2": "",
                "incomeChange": None,
                "incomeChangeReason": ""
            }
        ],
    },

}

goods = {
    "goods": [
        {"goodCost": 100.0, "goodModel": "Model1", "goodsDescription": "Description1", "goodType": "Type1"},
        {"goodCost": 50.0, "goodModel": "Model2", "goodsDescription": "Description2", "goodType": "Type2"}
    ]
}

data_request = sovcombank_connect_api_service.fill_templates_request(data, **filled_data, **goods)

if sovcombank_connect_api_service.validate_fields(data_request, REQUIRED_FIELDS, FIELD_TYPES, FIELD_RANGES, FIELD_ENUMS) and validate_goods_list(
        data_request):
    print(json.dumps(data_request, indent=4, ensure_ascii=False))
