# 3. Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#       *Пример:*
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.

n = int(input('Введите N: '))
dictionary = {i: round((1 + (1 / i)) ** i, 2) for i in range(1, n + 1)}

print(dictionary)
sumOfElementsInDictionary = 0
for i in dictionary:
    sumOfElementsInDictionary += dictionary[i]
print(f'Сумма всех элементов словаря равна: {sumOfElementsInDictionary}')
