def convert_speed(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует скорость между различными единицами измерения.

    Поддерживаемые единицы измерения скорости:
    - 'm/s'   — метры в секунду
    - 'km/h'  — километры в час
    - 'mph'   — мили в час (miles per hour)
    - 'knots' — узлы (морские мили в час)

    📘 Справка и формулы: https://www.metric-conversions.org/speed-conversion.htm

    Пример:
    convert_speed(100, 'km/h', 'mph')  # Переведёт 100 км/ч в мили в час

    :param value: Числовое значение скорости (например, 27.8)
    :param from_unit: В какой единице сейчас измеряется скорость (например, 'm/s')
    :param to_unit: В какую единицу нужно перевести (например, 'knots')
    :return: Скорость в целевой единице (float)
    """
    # Приведение всех значений к м/с, затем перевод в целевую единицу
    conversions = {
        'm/s': lambda x: x,           # Метры в секунду остаются неизменными
        'km/h': lambda x: x / 3.6,    # Километры в час в метры в секунду
        'mph': lambda x: x * 0.44704,# Мили в час в метры в секунду
        'knots': lambda x: x * 0.514444 # Морские мили в час в метры в секунду
    }

    # Обратные переводы из метров в секунду в целевые единицы
    reverse_conversions = {
        'm/s': lambda x: x,           # Метры в секунду остаются такими же
        'km/h': lambda x: x * 3.6,    # Метры в секунду в километры в час
        'mph': lambda x: x / 0.44704,# Метры в секунду в мили в час
        'knots': lambda x: x / 0.514444 # Метры в секунду в морские мили в час
    }

    # Сначала приводим значение к м/с
    intermediate_value = conversions.get(from_unit)(value)

    # Затем переводим промежуточное значение в целевую единицу
    converted_value = reverse_conversions.get(to_unit)(intermediate_value)

    return round(converted_value, 4)  # Округлим до четырёх знаков после запятой