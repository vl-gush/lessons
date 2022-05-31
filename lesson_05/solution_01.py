"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных, но
только если они не равны None. Получим, например, следующее сообщение:
Переданы аргументы: var1 = 2, var3 = 10.
"""


def three_args(var1=None, var2=None, var3=None):
    vars_dict = {}
    if var1 is not None:
        vars_dict["var1"] = var1
    if var2 is not None:
        vars_dict["var2"] = var2
    if var3 is not None:
        vars_dict["var3"] = var3
    result = [f"{key} = {vars_dict[key]}" for key in vars_dict.keys()]
    print(f"Переданы аргументы: {', '.join(result)}.")


three_args(var1=10, var2=None, var3=5)
