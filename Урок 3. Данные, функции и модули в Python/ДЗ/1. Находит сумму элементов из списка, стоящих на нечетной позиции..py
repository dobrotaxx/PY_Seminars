# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#       Пример:
#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

userList = list(input('Задайте список (через пробел, без запятых): ').split())
print(userList)
sumOfOddNum = 0
for i in range(0, len(userList)):
    if i % 2 != 0:
        sumOfOddNum += int(userList[i])
print(sumOfOddNum)
