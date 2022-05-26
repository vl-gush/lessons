# Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран. Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево

my_string = input("Введите строку: ")

index = 0
reverse_index = -1
message = "Yes"

while index != len(my_string) // 2 + 1:
    if my_string[index] != my_string[reverse_index]:
        message = "No"
        break
    else:
        index += 1
        reverse_index -= 1

print(message)
