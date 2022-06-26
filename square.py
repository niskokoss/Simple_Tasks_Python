# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.


import math


def square(side_of_a_square: int = ""):
    p_square = side_of_a_square * 4
    s_square = side_of_a_square * side_of_a_square
    d_square = side_of_a_square * math.sqrt(2)
    return p_square, s_square, d_square


if __name__ == "__main__":
    print(square(4))
    print(square(44))
    print(square(12))
    print(square(76))
