# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponent(a, b):
    if b == 1: return a
    if b != 1: return (a * exponent(a, b - 1))

num_a = int(input('Введите число А: '))
num_b = int(input('Введите число B: '))
print(f'{num_a} в степени {num_b} --> {exponent(num_a, num_b)}')
