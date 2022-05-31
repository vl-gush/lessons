"""
Написать функцию, которая получает на вход имя и выводит строку
вида: f"Hello, {name}". Создать список из 5 имен. Вызвать функцию для каждого
элемента списка в цикле.
"""


def greeting(name):
    print(f"Hello, {name}!")


names = ["Alex", "Bob", "John", "Julia", "Katy"]

for name in names:
    greeting(name)
