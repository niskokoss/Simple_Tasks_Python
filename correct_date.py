# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.


import datetime


def date(day: int = "", month: int = "", year: int = ""):
    try:
        x = datetime.date(year, month, day)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print(date(13, 10, 2022))
    print(date(31, 6, 1954))
    print(date(11, 1, 2018))
    print(date(32, 10, 2000))
