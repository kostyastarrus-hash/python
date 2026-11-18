"""Проверка продолжительности сна: меньше нормы, больше нормы или нормально."""

MIN_HOURS = 8
MAX_HOURS = 10

hours = int(input())

if hours < MIN_HOURS:
    print("Недосып")
elif hours > MAX_HOURS:
    print("Пересып")
else:
    print("Это нормально")
