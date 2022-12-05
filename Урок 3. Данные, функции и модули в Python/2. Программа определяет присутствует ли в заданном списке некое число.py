# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.

lst = ['blue', 'green', 'white', 'gr5y', 'red']
num = 5
answer = False
for i in lst:
    for j in i:
        if j == str(num):
            answer = True
            break
print(answer)
