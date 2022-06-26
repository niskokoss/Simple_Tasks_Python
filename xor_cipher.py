# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать,
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^)
# над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.


def xor_cipher(source_string: str = "", encryption_key: int = ""):
    encrypted_string = ''
    for i in source_string:
        encrypted_string += chr(ord(i) ^ encryption_key)
    return encrypted_string


if __name__ == "__main__":
    print(xor_cipher("Привет мир!", 123))
    print(xor_cipher(xor_cipher("Привет мир!", 123), 123))
    print(xor_cipher("Череповец", 13))
    print(xor_cipher(xor_cipher("Череповец", 13), 13))
