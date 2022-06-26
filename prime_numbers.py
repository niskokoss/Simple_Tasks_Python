# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.


def is_prime(number: int = ""):
    if number == 1:
        return False
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(97))
    print(is_prime(4))
    print(is_prime(37))
    print(is_prime(631))
    print(is_prime(111))

