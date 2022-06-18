import datetime


def how_many_days_to(x: str = ''):
    try:
        days_the_date1 = datetime.datetime.strptime(x, '%d.%m.%Y').date()
        local = datetime.date.today()
        print(type(local))

        if days_the_date1 > local:
            days_between = days_the_date1 - local
            return print("Сколько дней до", x + ":", days_between.days)
        else:
            raise ValueError(f'Дата в прошлом на {abs((days_the_date1 - local).days)} дней')
    except ValueError:
        raise ValueError('Введите дату')


if __name__ == "__main__":
    print(how_many_days_to("12.12.2023"))
    print(how_many_days_to("12.12.2022"))
    print(how_many_days_to("12.12.2021"))
    print(how_many_days_to("12.12.2tdf0"))


    
    
    
    
    
    
def calculation_of_money_per_day(x: int = "Деньги", y: int = "Дни"):
    return f'{round((x / y), 2)} руб/день'



if __name__ == "__main__":
    print(calculation_of_money_per_day(1000, 25))
    print(calculation_of_money_per_day(15000, 29))
    print(calculation_of_money_per_day(106684, 1243))

