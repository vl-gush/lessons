"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой
строчный символ, из этих чисел составляется первый список. Далее таким же
образом вводятся второй и третий списки. Вывести на экран список, элементы
которого есть в первых двух списках, но отсутствуют в третьем.
"""

list1 = []
list2 = []
list3 = []

for i in (list1, list2, list3):
    while True:
        num = input("Введите число: ")
        if num.isdigit():
            i.append(int(num))
        else:
            break

res = []

for i in (*list1, *list2):
    if i in list1 and i in list2 and i not in list3 and i not in res:
        res.append(i)

print(res)
