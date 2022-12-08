# 1. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

userList = list(map(int,input('Введите числа через пробел:').split()))
resultList = [int(i) for i in userList]
print(min(resultList),max(resultList))