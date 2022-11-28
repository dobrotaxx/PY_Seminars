# 4. Напишите программу, которая на вход принимает вещественное число и показывает сумму его чисел.

# number = int(input('Введите число: '))
# summa = 0
# while number > 0:
#     ostatok = number % 10
#     summa += ostatok
#     number //= 10
# print(summa)

number = float(input('Введите число: '))
while number % 1 != 0:
    number *= 10
summa = 0
while number > 0:
    ostatok = number % 10
    summa += ostatok
    number //= 10
print(int(summa))
