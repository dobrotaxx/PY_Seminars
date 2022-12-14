# Написать программу, которая находит НОК и НОД.

n1 = int(input('Введите первое число:'))
n2 = int(input('Введите второе число:'))

list_of_factor = []
list_of_factor2 = []


def Find_simple_factors(n, list):
    num_factor = 2
    while n > 1:
        if n % num_factor == 0:
            list.append(num_factor)
            n = int(n / num_factor)
        else:
            num_factor += 1


Find_simple_factors(n1, list_of_factor)
Find_simple_factors(n2, list_of_factor2)

# set() - создает множество, в котором убирает повторения

intersections_of_sets = set(list_of_factor).intersection(set(list_of_factor2))  # Множители для НОД
nod = 1
for i in intersections_of_sets:
    nod = nod * i
print(f'НОД равен: {nod}')

nok = int((n1 * n2)/nod)
print(f'НОК равен: {nok}')
