# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

users_list = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
new_list = []
count = 0
for i in range(0, len(users_list)):
    for j in range(0, len(users_list)):
        if users_list[j] == users_list[i]:
            count += 1
    if count <= 1:
        new_list.append(users_list[i])
    count = 0
print(new_list)
