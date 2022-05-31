"""
Создать функцию, которая принимает на вход неопределенное количество аргументов
и возвращает их сумму и максимальное из
них.
"""


def my_func(*args):
    result_sum = 0
    max_item = args[0]
    for item in args:
        result_sum += item
        if max_item < item:
            max_item = item
    return sum(args), max(args)


print(my_func(2, 5, 1, 7, 8, 9))
