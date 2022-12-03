# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

with open('file.txt', 'w') as data:
    data.write('232\n')
    data.write('75\n')
    data.write('8\n')
    data.write('19\n')
    data.write('5\n')

path = 'file.txt'
data = open(path, 'r')
result = 1
for line in data:
    print(line)
    result *= int(line)
print(result)
data.close()
