"""
Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент func_type. В
зависимости от func_type вернуть минимальное либо максимальное значение. Написать программу в виде трех функций.
"""


def my_func(func_type:str, *args):
    if func_type == "min":
        return my_min(*args)
    elif func_type == "max":
        return my_max(*args)


def my_max(*args):
    return max(args)


def my_min(*args):
    return min(args)


print(my_func('max', 4, 3, 5, 6, 6, 9))
