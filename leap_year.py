# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.


def is_year_leap(year: int = ""):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_year_leap(2044))
    print(is_year_leap(2042))
    print(is_year_leap(2022))
    print(is_year_leap(2012))
