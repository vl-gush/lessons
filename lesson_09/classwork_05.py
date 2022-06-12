"""
Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут, вывести на печать
результат.
"""

from classwork_02 import NewTime

if __name__ == "__main__":
    a = NewTime.seconds_to_time(800)
    b = NewTime.seconds_to_time(400)

    print(f"{a} - {b} = {a - b}")
