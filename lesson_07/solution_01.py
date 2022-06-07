"""
Используя условие первой задачи из урока, проверить то же самое только для коней.
"""


def is_figures_beat_each_other(x1, y1, x2, y2):
    return abs(abs(x1 - x2) - abs(y1 - y2)) == 1


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    if is_figures_beat_each_other(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
