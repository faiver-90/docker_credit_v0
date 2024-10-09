import copy
import json
import sys


class BankingRequestsService:
    def __init__(self, path_to_template):
        self.path_to_template = path_to_template
        self.template_data = self.load_json_template()

    def load_json_template(self):
        """Загрузка JSON-шаблона из файла."""
        try:
            with open(self.path_to_template, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {self.path_to_template} not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.path_to_template}.")
            sys.exit(1)

    @staticmethod
    def fill_templates_request(data, **kwargs):
        """
        Функция объединяет шаблон JSON с переданными данными, рекурсивно добавляя вложенные структуры.
        """
        combined_data = copy.deepcopy(data)  # Копируем данные, чтобы не модифицировать исходный шаблон

        def merge_dicts(dict1, dict2):
            """
            Рекурсивно объединяем два словаря.
            Если ключ присутствует в обоих словарях и является вложенным словарем, рекурсивно объединяем их.
            Если ключ — это список, заменяем существующий список новым.
            """
            for key, value in dict2.items():
                if isinstance(value, dict):
                    dict1[key] = merge_dicts(dict1.get(key, {}), value)
                elif isinstance(value, list):
                    # Если ключ — это список, заменяем его новым списком
                    dict1[key] = value
                else:
                    dict1[key] = value
            return dict1

        # Объединяем шаблон с новыми данными
        combined_data = merge_dicts(combined_data, kwargs)

        return combined_data

    @staticmethod
    def validate_required_fields(data, required_fields):
        """
        Функция для валидации обязательных полей.
        Проверяет, что все обязательные поля присутствуют и не пусты (значения не пустые строки, нулевые или None).
        """
        missing_fields = []

        def check_fields(d, required_fields):
            for field in required_fields:
                keys = field.split('.')
                temp = d
                for key in keys:
                    if isinstance(temp, dict) and key in temp:
                        temp = temp[key]
                    else:
                        missing_fields.append(field)
                        break
                # Проверка на пустые значения
                if temp is None or temp == "" or temp == 0:
                    missing_fields.append(field)

        check_fields(data, required_fields)

        if missing_fields:
            raise Exception(f"Следующие обязательные поля отсутствуют или пусты: {', '.join(missing_fields)}")

        return True
