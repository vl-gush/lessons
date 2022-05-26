"""
Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать также функцию
xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
"""


def xor_cipher(string, key):
    cipher = ""
    for i in string:
        cipher += chr(ord(i) ^ key)
    return cipher


def xor_uncipher(cipher, key):
    string = ""
    for i in cipher:
        string += chr(ord(i) ^ key)
    return string
