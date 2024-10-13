from apps.core.banking_services.sovcombank.sovcombank_factory_response_handlers import (SovcombankShotHandler,
                                                                                        SovcombankAgreementHandler,
                                                                                        SovcombankCalculationHandler,
                                                                                        SovcombankAssetHandler,
                                                                                        SovcombankDocumentsHandler,
                                                                                        SovcombankFullHandler,
                                                                                        SovcombankGetStatusHandler,
                                                                                        SovcombankInsuranceHandler,
                                                                                        SovcombankPostStatusHandler)


class SovcombankResponseHandlerFactory:
    """
    Фабрика для получения обработчиков ответов от различных эндпоинтов Sovcombank.

    Класс предоставляет обработчики для разных типов запросов, отправленных в Sovcombank.
    На основе эндпоинта (endpoint) возвращает соответствующий обработчик, который
    реализует логику обработки ответа.

    Атрибуты:
    ----------
    handlers : dict
        Словарь, который сопоставляет названия эндпоинтов (например, 'sovcombank_shot')
        с классами обработчиков (например, SovcombankShotHandler).
    """

    handlers = {
        "sovcombank_shot": SovcombankShotHandler,
        "sovcombank_agreement": SovcombankAgreementHandler,
        "sovcombank_calculation": SovcombankCalculationHandler,
        "sovcombank_asset": SovcombankAssetHandler,
        "sovcombank_documents": SovcombankDocumentsHandler,
        "sovcombank_full": SovcombankFullHandler,
        "sovcombank_post_status": SovcombankPostStatusHandler,
        "sovcombank_get_status": SovcombankGetStatusHandler,
        "sovcombank_insurance": SovcombankInsuranceHandler,
    }

    @staticmethod
    def get_handler(endpoint):
        """
        Возвращает обработчик для указанного эндпоинта.

        Если эндпоинт найден в словаре обработчиков, возвращается экземпляр
        соответствующего класса обработчика. Если эндпоинт не найден, возвращается None.

        Параметры:
        ----------
        endpoint : str
            Название эндпоинта, для которого нужно получить обработчик.

        Возвращает:
        -----------
        handler : object
            Экземпляр класса обработчика, связанного с указанным эндпоинтом, или None,
            если обработчик для эндпоинта не найден.
        """
        handler_class = SovcombankResponseHandlerFactory.handlers.get(endpoint, None)
        return handler_class()


class SovcombankEndpointResponseProcessor:
    def __init__(self):
        """
        Инициализация с фабрикой, которая будет возвращать обработчики для разных эндпоинтов.
        """
        self.factory = SovcombankResponseHandlerFactory()

    def handle_endpoint_response(self, endpoint, response):
        """
        Метод обработки ответов от разных эндпоинтов.
        """
        handler = self.factory.get_handler(endpoint)
        return handler.process_response(response)
