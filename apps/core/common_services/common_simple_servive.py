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
