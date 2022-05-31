"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно
зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную путем
применения функции XOR (^) над символами строки с ключом. Написать также
функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает
исходную строку.
"""


def xor_cipher(string, key):
    cipher = ""
    key = key * (len(string) // len(key) + 1)
    key = key[:len(string)]
    index = 0
    while index < len(string):
        cipher += chr(ord(string[index]) ^ ord(key[index]))
        index += 1
    return cipher


print(xor_cipher('text', '13'))
print(xor_cipher(xor_cipher('text', '13'), '13'))
