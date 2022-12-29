# # Улучшить код программы
# Принимает на вход дробь и показывать первую цифру дробной части числа
# num = float(input('Введите число: '))
# print(int((abs(num) % 1) * 10))

# Before
# num = input('Введите число: ')
# for i in range(len(num)):
#     if num[i] == ".":
#         print(num[i + 1])
#         break

# After
num = input('Введите число: ')
res = [print(num[i + 1]) for i in range(len(num)) if num[i] == "."]
