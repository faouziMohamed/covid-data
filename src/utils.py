from typing import Tuple


def today(as_string=True):
    from datetime import date
    today_ = date.today()
    if as_string:
        return str(today_)
    return today_.year, today_.month, today_.day


def is_leap_year(y):
    leap = False
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        leap = True
    return leap


def year_mon_day(a_date: str = today()) -> Tuple[int, int, int]:
    """
    Take a date as string in the format : yyy-mm-dd and
    return the respectively the date yyyy, mm and dd as int in a tuple
    :param a_date:
    :return: Respectively the date yyyy, mm and dd as int in a tuple
    """
    y, m, d = str(a_date).split('-')
    return int(y), int(m), int(d)


def days_in_month(a_date: str = today()):
    y, m, d = year_mon_day(a_date)
    if m in [4, 6, 9, 11]:
        total_days = 30
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        total_days = 31
    elif is_leap_year(y):
        total_days = 29
    else:
        total_days = 28
    return total_days


def day_after(a_date: str = today(), as_string=True):
    year, month, day = year_mon_day(a_date)
    day = day - 1
    if day == 0:
        month = month - 1
        if month == 0:
            year = year - 1
            month = 12
            day = 31
        day = days_in_month(f'{year}-{month}-{day}')

    if as_string:
        return f'{year}-{month}-{day}'
    else:
        return year, month, day


def yesterday(as_string=True):
    return day_after(today(), as_string=as_string)
