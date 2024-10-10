import copy
import json
import sys


class BankingBuildingRequestsService:
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

    def __init__(self, path_to_template):
        """
        Инициализация сервиса с указанием пути к файлу шаблона.

        Параметры:
        ----------
        path_to_template : str
            Путь к файлу с JSON-шаблоном.
        """
        self.path_to_template = path_to_template
        self.template_data = self.load_json_template()

    def load_json_template(self):
        """
        Загружает JSON-шаблон из указанного файла.

        Возвращает:
        -----------
        dict
            Шаблон в виде словаря.

        Исключения:
        -----------
        FileNotFoundError:
            Если файл не найден.

        JSONDecodeError:
            Если файл содержит некорректный JSON.
        """
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


class ValidateFieldService:
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
        errors = []

        # Проверка обязательных полей
        missing_fields = self.check_required_fields(data, required_fields)
        if missing_fields:
            errors.append(f"Следующие обязательные поля отсутствуют или пусты: {', '.join(missing_fields)}")

        # Проверка типов данных
        if field_types:
            incorrect_types = self.check_field_types(data, field_types)
            if incorrect_types:
                errors.append(f"Следующие поля имеют некорректные типы данных: {', '.join(incorrect_types)}")

        # Проверка диапазонов значений
        if field_ranges:
            out_of_range = self.check_field_ranges(data, field_ranges)
            if out_of_range:
                errors.append(f"Следующие поля вне допустимого диапазона: {', '.join(out_of_range)}")

        # Проверка допустимых значений
        if field_enums:
            invalid_values = self.check_enumerations(data, field_enums)
            if invalid_values:
                errors.append(f"Следующие поля содержат недопустимые значения: {', '.join(invalid_values)}")

        if errors:
            print(errors)
            raise Exception("\n".join(errors))

        return True

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

        def check_enumerations(d, field_enums):
            for field, allowed_values in field_enums.items():
                keys = field.split('.')
                temp = d
                for key in keys:
                    if isinstance(temp, dict) and key in temp:
                        temp = temp[key]
                    else:
                        invalid_values.append(f"{field} (отсутствует)")
                        break
                if temp not in allowed_values:
                    invalid_values.append(f"{field} (недопустимое значение: {temp})")

        check_enumerations(data, field_enums)
        return invalid_values

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

        def check_ranges(d, field_ranges):
            for field, (min_value, max_value) in field_ranges.items():
                keys = field.split('.')
                temp = d
                for key in keys:
                    if isinstance(temp, dict) and key in temp:
                        temp = temp[key]
                    else:
                        out_of_range.append(f"{field} (отсутствует)")
                        break
                if not (min_value <= temp <= max_value):
                    out_of_range.append(f"{field} (ожидалось в диапазоне {min_value}-{max_value}, получено {temp})")

        check_ranges(data, field_ranges)
        return out_of_range

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

        def check_types(d, field_types):
            for field, expected_type in field_types.items():
                keys = field.split('.')
                temp = d
                for key in keys:
                    if isinstance(temp, dict) and key in temp:
                        temp = temp[key]
                    else:
                        incorrect_types.append(f"{field} (отсутствует)")
                        break
                if not isinstance(temp, expected_type):
                    incorrect_types.append(
                        f"{field} (ожидалось {expected_type.__name__}, получено {type(temp).__name__})")

        check_types(data, field_types)
        return incorrect_types

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
                # Проверка на пустые, нулевые или неположительные значения
                if temp is None or temp == "" or temp == 0 or temp == 0.0 or (
                        isinstance(temp, (int, float)) and temp <= 0):
                    missing_fields.append(field)

        check_fields(data, required_fields)
        return missing_fields
