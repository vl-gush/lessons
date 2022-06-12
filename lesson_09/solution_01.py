"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), Triangle (атрибуты:
три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и
периметра). При потребности создавать все необходимые методы не описанные в задании.
"""

from __future__ import annotations
from math import pi, sqrt


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, centre: Point, radius: int):
        self.centre = centre
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def square(self) -> float:
        return (pi * self.radius) ** 2


class Triangle:

    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    @staticmethod
    def length_of_triangle_side(point1: Point, point2: Point) -> float:
        return sqrt(abs(point1.x - point2.x) + abs(point1.y - point2.y))

    def perimeter(self) -> float:
        side1 = Triangle.length_of_triangle_side(point1=self.point1, point2=self.point2)
        side2 = Triangle.length_of_triangle_side(point1=self.point2, point2=self.point3)
        side3 = Triangle.length_of_triangle_side(point1=self.point3, point2=self.point1)
        return side1 + side2 + side3

    def square(self) -> float:
        half_per = self.perimeter() / 2
        a = Triangle.length_of_triangle_side(point1=self.point1, point2=self.point2)
        b = Triangle.length_of_triangle_side(point1=self.point2, point2=self.point3)
        c = Triangle.length_of_triangle_side(point1=self.point3, point2=self.point1)
        return sqrt(half_per * (half_per - a) * (half_per - b) * (half_per - c))


class Square:

    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    @staticmethod
    def lenghts_of_sides(point1: Point, point2: Point) -> tuple:
        return abs(point1.x - point2.x) , abs(point1.y - point2.y)

    def perimeter(self) -> float:
        a, b = Square.lenghts_of_sides(point1=self.point1, point2=self.point2)
        return (a * b) * 2

    def square(self) -> float:
        a, b = Square.lenghts_of_sides(point1=self.point1, point2=self.point2)
        return a * b
