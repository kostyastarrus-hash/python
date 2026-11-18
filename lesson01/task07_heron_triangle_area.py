
"""Вычисление площади треугольника по формуле Герона с проверкой существования."""

import math


def heron_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по трём сторонам (формула Герона)."""
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    return None


a = int(input())
b = int(input())
c = int(input())

area = heron_triangle_area(a, b, c)

if area is not None:
    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Треугольник с такими сторонами не существует.")
