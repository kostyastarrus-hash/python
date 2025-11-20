f = str(input())
if f ==("Прямоугольник" or "прямоугольник"):
    a = int(input("Введите первое число"))
    b = int(input("Введите второе число"))
    print(a*b)
elif f == ("Трегольник" or "тругольник"):
    a = int(input("Введите первое число"))
    b = int(input("Введите второе число"))
    c = int(input("Введите третье число"))
    p = (a+b+c) / 2
    print ((p *(p- a) * (p-b)*(p-b))**0.5)
elif f == ("Круг" or "круг"):
    r = int(input())

print(3.14 * r **2)
