import logging

from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_get_status.sovcombank_get_status import \
    SovcombankGetStatusSendHandler

logger = logging.getLogger(__name__)

sovcombank_get_statusSend_handler = SovcombankGetStatusSendHandler()
collect_sovcom_status = sovcombank_get_statusSend_handler.description_list.keys()

COLLECTIONS_OFFER_STATUSES = list(collect_sovcom_status)
