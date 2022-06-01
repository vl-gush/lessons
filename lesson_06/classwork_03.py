"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт, где на первом месте
номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""
from random import choice


nominal = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
suit = ("Hearts", "Diamonds", "Clubs", "Spades")


def get_card():
    return choice(nominal), choice(suit)


for _ in range(5):
    print(get_card())
