import copy
import json
import logging
import sys

import requests

from apps.core.common_services.common_simple_service import error_message_formatter

logger = logging.getLogger(__name__)


class SovcombankRequestService:
    """
    Сервис для отправки запросов в Sovcombank.

    Этот класс формирует запросы к API Sovcombank, добавляет заголовки
    и отправляет данные.
    """

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.url = None

    def building_headers(self, endpoint, extra_headers=None):
        """
        Формирует URL и заголовки для запроса на указанный эндпоинт.

        Параметры:
        -----------
        endpoint : str
            URL-эндпоинт для запроса.
        """
        self.url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        if extra_headers:
            headers.update(extra_headers)
        return headers

    def send_request(self, method, headers, data=None):
        """
        Отправляет запрос в Sovcombank с заданными данными.

        Параметры:
        -----------
        method : str
        HTTP-метод запроса (например, 'POST').

        data : dict
        Данные, которые нужно отправить в запросе.

        Возвращает:
        -----------
        dict
        Ответ от Sovcombank.
        """
        response = requests.request(method,
                                    self.url,
                                    headers=headers,
                                    json=data)
        response.raise_for_status()

        # print('response', json.dumps(response.json(), indent=4, ensure_ascii=False))

        return response.json()


class CommonBankBuildingDataRequestsService:
    """
    Класс для работы с шаблонами запросов к банковским системам.

    Этот класс загружает шаблон JSON из файла и предоставляет метод для
    объединения шаблона с переданными данными.

    Атрибуты:
    ----------
    path_to_template : str
        Путь к файлу с JSON-шаблоном.

    template_data : dict
        Данные шаблона, загруженные из JSON-файла.

    Методы:
    --------
    load_json_template():
        Загружает JSON-шаблон из файла и возвращает его как словарь.

    fill_templates_request(data, **kwargs):
        Объединяет шаблон с переданными данными, заменяя значения в шаблоне.
    """

    def __init__(self, operation_id=None):
        """
        Инициализация сервиса с указанием пути к файлу шаблона.

        Параметры:
        ----------
        path_to_template : str
            Путь к файлу с JSON-шаблоном.
        """
        self.operation_id = operation_id

    def fill_templates_request(self, data, **kwargs):
        """
        Объединяет данные шаблона с переданными аргументами.

        Параметры:
        -----------
        data : dict
            Исходные данные шаблона.

        **kwargs : dict
            Новые данные, которые необходимо добавить или обновить в шаблоне.

        Возвращает:
        -----------
        dict
            Объединённый шаблон с новыми данными.
        """
        combined_data = copy.deepcopy(data)  # Копируем данные, чтобы не модифицировать исходный шаблон

        def merge_dicts(dict1, dict2):
            """
            Рекурсивно объединяет два словаря.
            При наличии одинаковых ключей значение обновляется.

            Параметры:
            ----------
            dict1 : dict
                Исходный словарь.

            dict2 : dict
                Словарь с новыми данными.

            Возвращает:
            -----------
            dict
                Объединённый словарь.
            """
            for key, value in dict2.items():
                if isinstance(value, dict):
                    dict1[key] = merge_dicts(dict1.get(key, {}), value)
                elif isinstance(value, list):
                    dict1[key] = value
                else:
                    dict1[key] = value
            return dict1

        # Объединяем шаблон с новыми данными
        combined_data = merge_dicts(combined_data, kwargs)

        return combined_data


class CommonValidateFieldService:
    """
    Сервис для валидации полей данных.

    Проверяет, что все обязательные поля присутствуют, имеют корректные типы данных,
    находятся в допустимых диапазонах значений и содержат допустимые значения (enumeration).

    Методы:
    --------
    validate_fields(data, required_fields, field_types=None, field_ranges=None, field_enums=None):
        Выполняет полную проверку данных на наличие обязательных полей, типов, диапазонов и допустимых значений.

    check_required_fields(data, required_fields):
        Проверяет, что все обязательные поля присутствуют и не пусты.

    check_field_types(data, field_types):
        Проверяет, что поля имеют правильные типы данных.

    check_field_ranges(data, field_ranges):
        Проверяет, что числовые поля находятся в заданном диапазоне.

    check_enumerations(data, field_enums):
        Проверяет, что поля содержат допустимые значения (enumeration).
    """

    def __init__(self, operation_id):
        self.operation_id = operation_id

    def validate_fields(self, data, required_fields, field_types=None, field_ranges=None, field_enums=None):
        """
        Выполняет полную проверку данных на наличие обязательных полей, корректных типов, диапазонов и допустимых значений.

        Параметры:
        ----------
        data : dict
            Данные, которые необходимо проверить.

        required_fields : list
            Список обязательных полей, которые должны присутствовать.

        field_types : dict, optional
            Словарь, где ключи — это имена полей, а значения — ожидаемые типы данных.

        field_ranges : dict, optional
            Словарь, где ключи — это имена полей, а значения — кортежи с минимальным и максимальным значением.

        field_enums : dict, optional
            Словарь, где ключи — это имена полей, а значения — списки допустимых значений.

        Возвращает:
        -----------
        bool
            Возвращает True, если все проверки пройдены.

        Исключения:
        -----------
        Exception:
            Если одна из проверок не пройдена, выбрасывается исключение с описанием ошибок.
        """
        try:
            missing_fields = self.check_required_fields(data, required_fields)
            if missing_fields:
                logger.error(
                    f"Следующие обязательные поля отсутствуют или пусты, {self.operation_id}: "
                    f"{', '.join(missing_fields)}")
                raise ValueError(
                    f"Некоторые обязательные поля пусты или отсутствуют. "
                    f"Поверьте заполненность обязательных полей и сохраните их.")

            # Проверка типов данных
            if field_types:
                incorrect_types = self.check_field_types(data, field_types)
                if incorrect_types:
                    logger.error(
                        f"Следующие поля имеют некорректные типы данных, {self.operation_id}: "
                        f"{', '.join(incorrect_types)}")
                    raise ValueError(f"Некоторые поля имеют некорректные типы данных. Проверьте корректность данных. "
                                     f"Проверьте корректность данных и сохраните их.")

            # Проверка диапазонов значений
            if field_ranges:
                out_of_range = self.check_field_ranges(data, field_ranges)
                if out_of_range:
                    logger.error(
                        f"Следующие поля вне допустимого диапазона, {self.operation_id}: "
                        f"{', '.join(out_of_range)}")
                    raise ValueError(f"Некоторые поля вне допустимого диапазона. Проверьте корректность данных. "
                                     f"Проверьте корректность данных и сохраните их.")

            # Проверка допустимых значений
            if field_enums:
                invalid_values = self.check_enumerations(data, field_enums)
                if invalid_values:
                    logger.error(
                        f"Следующие поля содержат недопустимые значения, {self.operation_id}: "
                        f"{', '.join(invalid_values)}")
                    raise ValueError(f"Некоторые поля содержат недопустимые значения. "
                                     f"Проверьте корректность данных и сохраните их.")

            return True

        except ValueError as e:
            massage = 'Ошибка валидации АПИ.'
            formatted_massage = error_message_formatter(massage,
                                                        e,
                                                        operation_id=self.operation_id)
            raise ValueError(formatted_massage)

    @staticmethod
    def check_enumerations(data, field_enums):
        """
        Проверяет, что поля содержат допустимые значения (enumeration).

        Параметры:
        ----------
        data : dict
            Данные, которые нужно проверить.

        field_enums : dict
            Словарь, где ключи — это имена полей, а значения — списки допустимых значений.

        Возвращает:
        -----------
        list
            Список полей, которые содержат недопустимые значения или отсутствуют.
        """
        invalid_values = []
        # try:
        for field, allowed_values in field_enums.items():
            keys = field.split('.')
            temp = data
            for key in keys:
                if isinstance(temp, dict) and key in temp:
                    temp = temp[key]
                else:
                    invalid_values.append(f"{field} (отсутствует)")
                    break
            if temp not in allowed_values:
                invalid_values.append(f"{field} (недопустимое значение: {temp})")
        return invalid_values

        # except Exception as e:
        #     logger.error(f"Ошибка проверки перечислений для поля {field}: {str(e)}")
        #     raise

    @staticmethod
    def check_field_ranges(data, field_ranges):
        """
        Проверяет, что числовые поля находятся в заданном диапазоне.

        Параметры:
        ----------
        data : dict
            Данные, которые нужно проверить.

        field_ranges : dict
            Словарь, где ключи — это имена полей, а значения — кортежи с минимальным и максимальным значением.

        Возвращает:
        -----------
        list
            Список полей, которые находятся вне допустимого диапазона.
        """
        out_of_range = []
        # try:
        for field, (min_value, max_value) in field_ranges.items():
            keys = field.split('.')
            temp = data
            for key in keys:
                if isinstance(temp, dict) and key in temp:
                    temp = temp[key]
                else:
                    out_of_range.append(f"{field} (отсутствует)")
                    break

            # Проверяем тип данных
            if isinstance(temp, (int, float)):
                if not (min_value <= temp <= max_value):
                    out_of_range.append(f"{field} (ожидалось в диапазоне {min_value}-{max_value}, получено {temp})")
            else:
                logger.error(f"Ошибка типа данных в поле {field}: ожидалось число, получено {type(temp).__name__}")
                out_of_range.append(f"{field} (ошибка типа данных: ожидалось число, получено {temp})")
        return out_of_range

        # except Exception as e:
        #     logger.error(f"Ошибка проверки диапазона для поля {field}: {str(e)}")
        #     raise

    @staticmethod
    def check_field_types(data, field_types):
        """
        Проверяет, что поля имеют правильные типы данных.

        Параметры:
        ----------
        data : dict
            Данные, которые нужно проверить.

        field_types : dict
            Словарь, где ключи — это имена полей, а значения — ожидаемые типы данных.

        Возвращает:
        -----------
        list
            Список полей с некорректными типами данных.
        """
        incorrect_types = []
        # try:
        for field, expected_type in field_types.items():
            keys = field.split('.')
            temp = data
            for key in keys:
                if isinstance(temp, dict) and key in temp:
                    temp = temp[key]
                else:
                    incorrect_types.append(f"{field} (отсутствует)")
                    break
            if not isinstance(temp, expected_type):
                incorrect_types.append(
                    f"{field} (ожидалось {expected_type.__name__}, получено {type(temp).__name__})")
        return incorrect_types

        # except Exception as e:
        #     logger.error(f"Ошибка проверки типов для поля {field}: {str(e)}")
        #     raise

    @staticmethod
    def check_required_fields(data, required_fields):
        """
        Проверяет, что все обязательные поля присутствуют и не пусты.

        Параметры:
        ----------
        data : dict
            Данные, которые нужно проверить.

        required_fields : list
            Список обязательных полей.

        Возвращает:
        -----------
        list
            Список отсутствующих или пустых полей.
        """
        missing_fields = []
        # try:
        for field in required_fields:
            keys = field.split('.')
            temp = data
            for key in keys:
                if isinstance(temp, dict) and key in temp:
                    temp = temp[key]
                else:
                    missing_fields.append(field)
                    break
            if isinstance(temp, bool):
                continue

            if temp is None or temp == "" or temp == 0:
                missing_fields.append(field)
        return missing_fields

        # except Exception as e:
        #     logger.error(f"Ошибка проверки обязательных полей: {str(e)}")
        #     raise
