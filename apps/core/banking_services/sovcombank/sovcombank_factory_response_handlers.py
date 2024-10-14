class SovcombankShotHandler:
    """
    Обработчик для ответа от Sovcombank по заявке (shot).

    Этот класс отвечает за обработку данных, полученных от API Sovcombank,
    для запроса 'shot'.
    """
    def process_response(self, response):
        """
        Обрабатывает ответ на запрос 'sovcombank_shot'.

        Параметры:
        -----------
        response : dict
            Ответ от API Sovcombank.

        Возвращает:
        -----------
        str
            Результат обработки ответа.
        """
        print("Обрабатываем ответ для 'sovcombank_shot'")
        return f"Результат обработки SovcombankShot: {response}"


class SovcombankAgreementHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_agreement'")
        return f"Результат обработки SovcombankAgreement: {response}"


class SovcombankCalculationHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_calculation'")
        return f"Результат обработки SovcombankCalculation: {response}"


class SovcombankAssetHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_asset'")
        return f"Результат обработки sovcombank_asset: {response}"


class SovcombankDocumentsHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_documents'")
        return f"Результат обработки sovcombank_documents: {response}"


class SovcombankFullHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_full'")
        return f"Результат обработки sovcombank_full: {response}"


class SovcombankGetStatusHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_get_status'")
        return f"Результат обработки sovcombank_get_status: {response}"


class SovcombankPostStatusHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_post_status'")
        return f"Результат обработки sovcombank_post_status: {response}"


class SovcombankInsuranceHandler:
    def process_response(self, response):
        print("Обрабатываем ответ для 'sovcombank_insurance'")
        return f"Результат обработки sovcombank_insurance: {response}"
