from app_v0.settings import BASE_DIR
from apps.core.banking_services.sovcombank.sovcombank_services.building_bank_requests_service import \
    BankingBuildingRequestsService, ValidateFieldService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_connect_api_service import \
    SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor

validate_service = ValidateFieldService()
sovcombank_request_service = SovcombankRequestService()

sovcombank_build_request_service = BankingBuildingRequestsService(
    f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_get_status.json')

application_id_from_db = '2' * 64  # приходит из бд, после отправки в shot

data_from_file = sovcombank_build_request_service.template_data

application_id_info = {
    'applicationId': application_id_from_db
}
data_request = sovcombank_build_request_service.fill_templates_request(data_from_file, **application_id_info)

REQUIRED_FIELDS = {
    "applicationId"
}
FIELD_TYPES = {
    "applicationId": str
}

if validate_service.validate_fields(data_request, REQUIRED_FIELDS, FIELD_TYPES):
    response = sovcombank_request_service.send_request(data_request)
    if response.get('status_code') == 200:
        result_get_status = endpoint_processor.handle_endpoint_response("sovcombank_get_status", response)
        print(result_get_status)
    else:
        raise ValueError(f"Ошибка при отправке запроса: {response.status_code}")
