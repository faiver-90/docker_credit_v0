from app_v0.settings import BASE_DIR
from apps.core.banking_services.sovcombank.response_handler_factory import (
    SovcombankResponseHandlerFactory, SovcombankEndpointResponseProcessor)
from apps.core.banking_services.sovcombank.sovcombank_services.building_bank_requests_service import (
    BankingBuildingRequestsService,
    ValidateFieldService)
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_connect_api_service import \
    SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services. \
    sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES, FIELD_RANGES, FIELD_ENUMS, REQUIRED_FIELDS

sovcombank_request_service = SovcombankRequestService()
validate_service = ValidateFieldService()

sovcombank_build_request_service = BankingBuildingRequestsService(
    f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')

data = sovcombank_build_request_service.template_data

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

data_request = sovcombank_build_request_service.fill_templates_request(
    data,
    **goods,
    **application_info,
    **source_system_info,
    **credit_info,
    **person_info
)

if validate_service.validate_fields(
        data_request,
        REQUIRED_FIELDS,
        FIELD_TYPES,
        FIELD_RANGES,
        FIELD_ENUMS
):
    # print(json.dumps(data_request, indent=4, ensure_ascii=False))
    response = sovcombank_request_service.send_request(data_request)
    factory = SovcombankResponseHandlerFactory()
    endpoint_processor = SovcombankEndpointResponseProcessor(factory)

    if response.get('status_code') == 200:
        result_shot = endpoint_processor.handle_endpoint_response("sovcombank_shot", response)
    else:
        raise ValueError(f"Ошибка при отправке запроса: {response.status_code}")
