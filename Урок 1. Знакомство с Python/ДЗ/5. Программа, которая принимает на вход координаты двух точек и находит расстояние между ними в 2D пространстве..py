# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
#                 - A (3,6); B (2,1) -> 5,09
#                 - A (7,-5); B (1,-1) -> 7,21
import math

def inputFloat(prompt=None):
    while True:
        usersNum = input(prompt)
        try:
            return float(usersNum)
        except ValueError:
            print(f'Вы ввели {usersNum}. Ожидалось вещественное число.')

xForPointA = inputFloat('Введите x для точки A: ')
yForPointA = inputFloat('Введите y для точки A: ')
xForPointB = inputFloat('Введите x для точки B: ')
yForPointB = inputFloat('Введите y для точки B: ')

print(math.sqrt((xForPointB - xForPointA)**2+(yForPointB - yForPointA)**2))
