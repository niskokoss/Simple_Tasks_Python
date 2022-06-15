import datetime


def how_many_days_to(x: str = ''):
    print(x)
    try:
        days_the_date1 = datetime.datetime.strptime(x, '%d.%m.%y')
        print(days_the_date1)
        if days_the_date1 > datetime.date:
            days_between = days_the_date1 - datetime.date.today()
            return days_between
        else:
            raise ValueError('Дата в прошлом')
    except:
        raise ValueError('Введите дату')


if __name__ == "__main__":
    how_many_days_to("12.12.22")
