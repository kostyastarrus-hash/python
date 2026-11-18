"""Практика: переменные, типы данных, цепное присваивание, операции со списками."""

my_list = ["start", "stop"]

first_num = 5.2
var = third_num = first_num + 7.8   # цепное присваивание: 13.0 попадает в две переменные
first_num += 5
second_num = 7.8
second_num += first_num
second_num = 10

my_list *= 5   # список повторяется 5 раз
print(my_list)
