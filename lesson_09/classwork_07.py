"""
Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

from classwork_06 import MyDateTime

if __name__ == "__main__":
    a = MyDateTime.seconds_to_time(125368566)
    print(a)
    print(a * 2)
