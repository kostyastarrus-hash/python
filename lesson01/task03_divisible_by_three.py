"""Проверка делимости двух чисел на 3: оба, одно или ни одного."""

chislo_1 = int(input())
chislo_2 = int(input())

if chislo_1 % 3 == 0 and chislo_2 % 3 == 0:
    print(True)
elif chislo_1 % 3 == 0 or chislo_2 % 3 == 0:
    print("Одно число делится на три")
else:
    print(False)
