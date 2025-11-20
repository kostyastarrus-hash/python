import math
a = int(input)
b = int(input)
c = int(input)

def heron_triangle_area(a, b, c):
  """
  Вычисляет площадь треугольника по формуле Герона.

  Args:
    a: Длина первой стороны.
    b: Длина второй стороны.
    c: Длина третьей стороны.

  Returns:
    Площадь треугольника или сообщение об ошибке, если треугольник не существует.
  """
  
  if a + b > c and a + c > b and b + c > a:

    p = (a + b + c) / 2

    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
  else:
    return "Треугольник с такими сторонами не существует."
side_a = 5
side_b = 6
side_c = 7

area = heron_triangle_area(side_a, side_b, side_c)

if isinstance(area, float):
  print(f"Площадь треугольника: {area:.2f}")
else:
  print(area)
