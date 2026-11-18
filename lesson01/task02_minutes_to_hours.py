"""Перевод минут в часы и остаток минут (целочисленное деление и остаток)."""

total_minutes = int(input())

hours = total_minutes // 60
minutes = total_minutes % 60

print(hours)
print(minutes)
