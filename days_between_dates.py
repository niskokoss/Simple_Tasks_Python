import datetime


def days_between_dates():
    the_date1 = input()
    try:
        the_date1 = the_date1.split(".")
        days_the_date1 = datetime.date(int(the_date1[0]), int(the_date1[1]), int(the_date1[2]))
        if days_the_date1 > datetime.date.today():
            days_between = days_the_date1 - datetime.date.today()
            return print(days_between)
        else:
            raise ValueError('Дата в прошлом')
    except:
        raise ValueError('Введите дату')

days_between_dates()
