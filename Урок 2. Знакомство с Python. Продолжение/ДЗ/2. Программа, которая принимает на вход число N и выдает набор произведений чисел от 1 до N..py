# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
N = int(input('Введите число N: '))
count = 0
result = 1
print(end = '[')
while N != 1:
    N -= 1
    count += 1
    result *= count
    print(end = f'{result}, ')
count += 1
result *= count
print(end = f'{result}]')



