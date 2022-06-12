"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

from solution_01 import Circle, Triangle, Square, Point


figures = [
    Circle(Point(10, 2), 15),
    Triangle(Point(2, 3), Point(15, 4), Point(22, 30)),
    Square(Point(1, 3), Point(41, 20))
]

for i in figures:
    print(i.perimeter())
    print(i.square())
