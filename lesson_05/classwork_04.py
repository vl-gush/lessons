"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к
которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".
"""


def month_to_season(number_of_month:int) -> str:
    seasons = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
    for season, months in seasons.items():
        if number_of_month in months:
            return season


print(month_to_season(12))
print(month_to_season(4))
print(month_to_season(7))
print(month_to_season(10))
