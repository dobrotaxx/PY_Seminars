# num = float(input('Введите число: '))
# print(int((abs(num) % 1) * 10))

num = input('Введите число: ')
for i in range(len(num)):
    if num[i] == ".":
        print(num[i + 1])
        break