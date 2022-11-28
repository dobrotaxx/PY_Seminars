# N = int(input('Введите число N = '))
# nums = []
# for i in range(-abs(N), abs(N) + 1, 1): # abs - функция выдает модуль числа
#     nums.append(i)
# print(nums)

N = int(input('Введите число N = '))
for i in range(-abs(N), abs(N) + 1, 1):
    print(i, end = ' ') # по умолчанию end = '\n' - (перенос строки)

