import datetime


def how_many_days_to(x, date: str = ''):
    try:
        days_the_date1 = datetime.datetime.strptime(x, '%y.%m.%d')
        if days_the_date1 > datetime.date.today():
            days_between = days_the_date1 - datetime.date.today()
            return days_between
        else:
            raise ValueError('Дата в прошлом')
    except:
        raise ValueError('Введите дату')


if __name__ == "__main__":
    how_many_days_to(input())
