# # Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# # Пример:
# #     - [2, 3, 4, 5, 6] => [12, 15, 16];
# #     - [2, 3, 5, 6] => [12, 15]
import math

def NewList(userList):
    lengthOfNewList = math.ceil(len(userList) / 2)
    finallyList = []
    for i in range(lengthOfNewList):
        if i != (len(userList) - i - 1):
            newList = userList[i] * userList[(len(userList) - i) - 1]
            finallyList.append(newList)
        else:
            newList *= userList[i]
            finallyList.append(newList)
    print(finallyList)


userList = list(map(int, input('Задайте список (через пробел, без запятых): ').split()))
print(userList)
NewList(userList)
