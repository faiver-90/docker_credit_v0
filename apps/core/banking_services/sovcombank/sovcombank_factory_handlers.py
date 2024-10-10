class SovcombankShotHandler:
    def process_response(self, response):
        # Логика обработки ответа для "sovcombank_shot"
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
