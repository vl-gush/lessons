"""
В школе решили набрать три новых класса по программированию. Так как занятия у них проходят в одно и то же время, было
решено выделить кабинет для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько
всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
количество учащихся в каждом из трех классов.
"""


def number_of_desk(class1, class2, class3):
    counter = 0
    for i in (class1, class2, class3):
        counter += i // 2
        if i % 2 == 1:
            counter += 1
    return counter