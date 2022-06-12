"""
Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
"""

from classwork_02 import NewTime

if __name__ == "__main__":
    a = NewTime.seconds_to_time(150)
    print(a)
    print(a * 2)
