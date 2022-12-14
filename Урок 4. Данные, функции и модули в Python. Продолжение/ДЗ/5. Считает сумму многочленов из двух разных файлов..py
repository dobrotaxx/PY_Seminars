# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    line1 = f1.readline()
    line2 = f2.readline()
    print(f' {line1}\n', f'{line2}\n')

lst = line1.split(' = ')[0]
print(lst)
lst2 = line2.split(' = ')[0]
print(lst2)
lst = lst.split(' + ')
lst2 = lst2.split(' + ')
print(lst)
print(lst2)

dict1 = {}
dict2 = {}

for i in range(len(lst)):
    if lst[i].count('x^'):
        dict1[int(lst[i].split('^')[1])] = int(lst[i].split('*')[0])
    elif lst[i].count('x'):
        dict1[1] = int(lst[i].split('*')[0])
    else:
        dict1[0] = int(lst[i])
print(dict1)

for i in range(len(lst2)):
    if lst2[i].count('x^'):
        dict2[int(lst2[i].split('^')[1])] = int(lst2[i].split('*')[0])
    elif lst2[i].count('x'):
        dict2[1] = int(lst2[i].split('*')[0])
    else:
        dict2[0] = int(lst2[i])
print(dict2)

max_index = 0
for key in dict1.keys():
    if max_index < key:
        max_index = key

for key in dict2.keys():
    if max_index < key:
        max_index = key

dict3 = {}
for i in range(max_index, -1, -1):
    if i in dict1:
        if i in dict2:
            dict3[i] = dict1[i] + dict2[i]
        else:
            dict3[i] = dict1
    elif i in dict2:
        dict3[i] = dict2
print(dict3)

result = []
for i in range(max_index, -1, -1):
    if i in dict3:
        if i == 1:
            result.append(str(dict3[i]) + ' * x')
        elif i == 0:
            result.append(str(dict3[i]))
        else:
            result.append(str(dict3[i]) + ' * x^' + str(i))

with open('file3.txt', 'w') as data:
    print(*result, file=data, sep=' + ', end=' = 0\n')
