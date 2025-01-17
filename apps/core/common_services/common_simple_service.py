import inspect
import json
import logging
import time
import uuid

from celery.result import AsyncResult

logger = logging.getLogger(__name__)


def convert_str_list(li):
    print(f'convert work')
    # return list(map(int, li[0].split(',')))
    return [int(x) for x in li[0].split(',') if x.strip().isdigit()]


def convert_value(value, target_type, default=None):
    """
    Универсальная функция для приведения данных к указанному типу с дефолтным значением для каждого типа.

    Параметры:
    ----------
    value : any
        Данные, которые нужно привести к нужному формату.
    target_type : type
        Тип, к которому нужно привести данные (str, int, float, bool).
    default : any, optional
        Значение по умолчанию, если данные не могут быть приведены к нужному типу.
        Если не указано, будет использоваться стандартное значение по умолчанию для каждого типа.

    Возвращает:
    -----------
    any
        Приведённые данные или значение по умолчанию, если преобразование не удалось.
    """
    # Определение дефолтного значения по умолчанию для каждого типа, если оно не указано явно
    default_values = {
        str: "",
        int: 0,
        float: 0.0,
        bool: False,
    }

    # Если дефолтное значение не указано, используем дефолт для данного типа
    if default is None:
        default = default_values.get(target_type, None)

    try:
        # Проверяем, если значение None, возвращаем дефолтное значение
        if value is None:
            return default

        # Если тип уже соответствует целевому, возвращаем как есть
        if isinstance(value, target_type):
            return value

        # Приведение к нужному типу
        return target_type(value)

    except (ValueError, TypeError):
        # Возвращаем дефолтное значение в случае ошибки преобразования
        return default


def create_uuid():
    return uuid.uuid4()


def get_operation_id(existing_operation_id=None):
    """
    Возвращает текущий operation_id или создает новый, если он не был передан.

    Параметры:
    ----------
    existing_operation_id : str, optional
        Существующий operation_id, если есть.

    Возвращает:
    ----------
    str
        Новый или существующий operation_id.
    """
    if existing_operation_id:
        return existing_operation_id
    return str(f'ID операции - {create_uuid()}')


def load_file(path_to_file, mode='r'):
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
    with open(path_to_file, mode, encoding='utf-8') as f:
        return json.load(f)


def get_local_var_for_exception():
    """
    Возвращает форматированный список локальных переменных из фрейма, предшествующего вызову функции,
    исключая переменные 'self' и 'e', которые могут не относиться к обработке исключений.

    Функция полезна для логирования и отладки при возникновении исключений, так как она предоставляет
    контекст локальных переменных, доступных на момент ошибки.

    Возвращает:
    -----------
    str:
        Строка, содержащая список локальных переменных и их значений, где каждая переменная отображается с новой строки.
        Пример:
        "variable_1: 'значение_1'\nvariable_2: 'значение_2'"
    """
    frame = inspect.currentframe().f_back
    local_variables = inspect.getargvalues(frame).locals
    filtered_variables = {key: repr(value) for key, value in local_variables.items()
                          if key not in ('self', 'e')}
    formatted_variables = '\n'.join([f'{key}: {value}' for key, value in filtered_variables.items()])

    return formatted_variables


def error_message_formatter(message=None, e=None, **kwargs):
    """
    Форматирует сообщение для логирования или исключения, добавляя описание ошибки и дополнительные данные.

    Параметры:
    ----------
    message : str
        Основное сообщение об ошибке.
    e : Exception
        Исключение, содержащее информацию об ошибке.
    **kwargs : dict
        Дополнительные данные в формате ключ-значение, которые будут добавлены в лог.

    Возвращает:
    -----------
    str
        Полностью отформатированное сообщение с описанием ошибки и дополнительными данными.
    """
    # Создаем список для итогового сообщения, избегая дублирования
    message_parts = []

    # Добавляем основное сообщение, если оно есть
    if message:
        message_parts.append(f"{message}")

    # Добавляем сообщение об исключении, если оно есть
    if e:
        message_parts.append(f"{str(e)}")

    # Форматируем дополнительные данные из kwargs, если они есть
    if kwargs:
        formatted_data = '\n'.join([f"{key}: {value}" for key, value in kwargs.items()])
        message_parts.append(f"\n{formatted_data}")

    # Объединяем все части сообщения в одну строку с новой строкой между частями
    return '\n'.join(message_parts)

def poll_task(task_id):
    task_result = AsyncResult(task_id)
    while task_result.state in ['PENDING', 'STARTED']:
        print(f"Текущий статус: {task_result.state}")
        time.sleep(5)  # Ожидаем 5 секунд перед следующим запросом
        task_result = AsyncResult(task_id)  # Обновляем состояние задачи

    if task_result.state == 'SUCCESS':
        print(f"Задача завершена:{task_result.result}")
        return task_result.result
    elif task_result.state == 'FAILURE':
        print(f"Задача завершилась ошибкой:{task_result.result}")
        return task_result.result