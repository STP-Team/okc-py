import datetime

time_format = "%d.%m.%Y"


def get_week_start_date() -> datetime.datetime:
    """
    Возвращает начало недели (понедельник) для парсинга KPI.

    Логика:
    - Если сегодня понедельник, парсим с этого понедельника
    - Если любой другой день недели, парсим с понедельника текущей недели

    Returns:
        datetime объект с началом недели (понедельник)
    """
    current_date = datetime.datetime.now()
    current_weekday = current_date.weekday()  # 0 = Понедельник, 6 = Воскресенье

    # Находим понедельник текущей недели
    days_since_monday = current_weekday
    monday_date = current_date - datetime.timedelta(days=days_since_monday)

    return monday_date.replace(hour=0, minute=0, second=0, microsecond=0)


def get_week_end_date() -> datetime.datetime:
    """
    Возвращает конец недели (воскресенье) для парсинга KPI.

    Returns:
        datetime объект с концом недели (воскресенье)
    """
    monday = get_week_start_date()
    sunday = monday + datetime.timedelta(days=6)
    return sunday.replace(hour=23, minute=59, second=59, microsecond=999999)
