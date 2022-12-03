# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.(Сделать для строки)
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11

def sum(num):
    if float(num) < 0:
        num = float(num) * (-1)
    number = 0

    for i in str(num):
        if i != '.':
            number += int(i)
    return number

num = str(input('Введите вещественное число: '))

print(f'Сумма цифр в числе {num} равна: {sum(num)}')
