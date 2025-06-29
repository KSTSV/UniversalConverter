def grams_to_kilograms(value: float) -> float:
    """
    Переводит массу из граммов в килограммы.

    Формула: кг = г / 1000

    📘 Справка по переводам масс: https://www.metric-conversions.org/weight-conversion.htm

    :param value: Масса в граммах (например, 500)
    :return: Масса в килограммах (например, 0.5)
    """
    return value / 1000


def kilograms_to_pounds(value: float) -> float:
    """
    Переводит массу из килограммов в фунты.

    Формула: фунты = кг × 2.20462

    📘 Справка по переводам масс: https://www.metric-conversions.org/weight-conversion.htm

    :param value: Масса в килограммах (например, 70)
    :return: Масса в фунтах (например, 154.32)
    """
    return value * 2.20462


def pounds_to_ounces(value: float) -> float:
    """
    Переводит массу из фунтов в унции.

    Формула: унции = фунты × 16

    📘 Справка по переводам масс: https://www.metric-conversions.org/weight-conversion.htm

    :param value: Масса в фунтах (например, 2)
    :return: Масса в унциях (например, 32)
    """
    return value * 16


def ounces_to_grams(value: float) -> float:
    """
    Переводит массу из унций в граммы.

    Формула: граммы = унции × 28.3495

    📘 Справка по переводам масс: https://www.metric-conversions.org/weight-conversion.htm

    :param value: Масса в унциях (например, 3.5)
    :return: Масса в граммах (например, 99.22)
    """
    return value * 28.3495