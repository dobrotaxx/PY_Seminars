# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    line1 = f1.readline()
    line2 = f2.readline()
    print(f' {line1}\n',f'{line2}\n')

lst = line1.split(' = ')[0]
lst2 = line2.split(' = ')[0]

lst = lst.split('x^')
lst = ''.join(lst)
lst = lst.split()

lst2 = lst2.split('x^')
lst2 = ''.join(lst2)
lst2 = lst2.split()


lst3 = []
lst4 = []
for i in lst:
    if i.isdigit():
        lst3.append(i)

lst3 = list(map(int, lst3))

for i in lst2:
    if i.isdigit():
        lst4.append(i)

lst4 = list(map(int, lst4))

result = []
for i in range(0, len(lst3)):
    if i % 2 == 0:
        if i == len(lst3)-1:
            result.append(f'{lst3[i] + lst4[i]}')
        else:
            result.append(f'{lst3[i] + lst4[i]} * x^')
    else:
        if i == len(lst3)-1:
            result.append(f'{lst3[i] + lst4[i]}')
        else:
            result.append(f'{lst3[i] + lst4[i]} + ')
result.append(' = 0')
result = ''.join(result)
print(result)

with open('file3.txt', 'w') as data:
    data.writelines(result)
