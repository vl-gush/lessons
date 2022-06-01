"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла, где на каждой строке пары слов вида:
apple,яблоко.
"""


import csv


with open("dictionary.csv", "r") as file:
    reader = csv.reader(file)

    my_dict = {
        row[0]: row[1]
        for row in reader
    }