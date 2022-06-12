"""
Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты: day, month, year.
“Исправить” все магические методы для этого класса.
4:0:11:0:36:6
"""

from __future__ import annotations
from classwork_02 import NewTime


class MyDateTime(NewTime):

    def __init__(self, year: int, month: int, day: int, hours: int, minutes: int, seconds: int):
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def seconds_to_time(seconds: int) -> MyDateTime:
        year = seconds // (30 * 12 * 24 * 60 * 60)
        if year > 0:
            seconds -= 30 * 12 * 24 * 60 * 60 * year
        month = seconds // (30 * 24 * 60 * 60)
        if month > 0:
            seconds -= 30 * 24 * 60 * 60 * month
        day = seconds // (24 * 60 * 60)
        if day > 0:
            seconds -= 24 * 60 * 60 * day
        hours = seconds // (60 * 60)
        if hours > 0:
            seconds -= 60 * 60 * hours
        minutes = seconds // 60
        if minutes > 0:
            seconds -= 60 * minutes
        return MyDateTime(year=year, month=month, day=day, hours=hours, minutes=minutes, seconds=seconds)
    
    def to_seconds(self) -> int:
        sec_in_min = 60
        sec_in_hour = 60 * 60
        sec_in_day = 60 * 60 * 24
        sec_in_month = 60 * 60 * 24 * 30
        sec_in_year = 60 * 60 * 24 * 30 * 12
        return (self.seconds + self.minutes * sec_in_min +
                self.hours * sec_in_hour + self.day * sec_in_day +
                self.month * sec_in_month + self.year * sec_in_year)

    def __add__(self, other: MyDateTime) -> MyDateTime:
        seconds = self.to_seconds() + other.to_seconds()
        return MyDateTime.seconds_to_time(seconds)

    def __sub__(self, other: MyDateTime) -> MyDateTime:
        seconds = self.to_seconds() - other.to_seconds()
        return MyDateTime.seconds_to_time(seconds)

    def __mul__(self, other: int) -> MyDateTime:
        seconds = self.to_seconds() * other
        return MyDateTime.seconds_to_time(seconds)

    def __str__(self) -> str:
        return f"{self.year}:{self.month}:{self.day}:{self.hours}:{self.minutes}:{self.seconds}"


if __name__ == "__main__":
    a = MyDateTime.seconds_to_time(125368566)
    print(a)
