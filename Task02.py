# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)

num_a = int(input('Введите число a: '))
num_b = int(input('Введите число b: '))
print(f'Сумма чисел {num_a} и {num_b} --> {summa(num_a, num_b)}')