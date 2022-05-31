"""
Написать функцию принимающая на вход неопределенным количеством аргументов и
именованный аргумент func_type. В зависимости от func_type вернуть минимальное
либо максимальное значение. Написать программу в виде трех функций.
"""


def my_func(func_type: str, *args):
    if func_type == "min":
        return my_min(*args)
    elif func_type == "max":
        return my_max(*args)


def my_max(*args):
    max_item = args[0]
    for item in args[1:]:
        if item > max_item:
            max_item = item
    return max_item


def my_min(*args):
    min_item = args[0]
    for item in args[1:]:
        if item < min_item:
            min_item = item
    return min_item


print(my_func('min', 4, 3, 5, 6, 6, 9))
