# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

userNum = int(input('Введите число: '))
newNum = ""
while userNum != 0:
    newNum = str(userNum % 2) + newNum
    userNum //= 2
print(newNum)
