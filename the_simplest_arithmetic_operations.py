# Простейшие арифметические операции

# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic(number_one: int = "", number_two: int = "", operation: str = ""):
    if operation == "+":
        return number_one + number_two
    elif operation == "-":
        return number_one - number_two
    elif operation == "*":
        return number_one * number_two
    elif operation == "/":
        return number_one / number_two
    else:
        return "Неизвестная операция"


if __name__ == "__main__":
    print(arithmetic(5, 2, "+"))
    print(arithmetic(6, 3, "-"))
    print(arithmetic(8, 3, "*"))
    print(arithmetic(12, 5, "/"))
    print(arithmetic(12, 4, "fd"))
