"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся
небольшие записки с именами участников. Затем каждый играющий по очереди
вытягивает бумажку с именем того, кому предстоит вручить презент. Ваша
программа должна используя список имен участников выдать на выходе пары,
кто и кому будет дарить, причем сам себе человек не может подарить, дубликаты
тоже не допустимы.
"""
from random import randint


def secret_santa(*args):
    givers = list(args).copy()
    getters = list(args).copy()
    pairs = []
    while givers:
        giver = givers[randint(0, len(givers) - 1)]
        getter = getters[randint(0, len(getters) - 1)]
        while giver == getter:
            getter = getters[randint(0, len(getters) - 1)]
        pairs.append(f"{giver} -> {getter}")
        givers.remove(giver)
        getters.remove(getter)
    return "\n".join(pairs)


print(secret_santa("Dave", "Alex", "John", "Julia", "Hellen", "Hannah"))
