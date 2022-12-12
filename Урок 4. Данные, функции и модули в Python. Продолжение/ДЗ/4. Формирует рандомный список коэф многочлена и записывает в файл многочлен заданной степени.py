# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)* многочлена и
# записать в файл многочлен степени k.
#     *Пример:*
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
from random import randint

k = 3
coefficients = [randint(0, 100) for i in range(0, k)]
result = []

j = 0
while k != 0:
    result.extend((f'{coefficients[j]}*x^{k}', ' ', '+', ' '))
    j += 1
    k -= 1
result.append(f'{randint(0, 100)} = 0')
with open('file.txt', 'w') as data:
    data.writelines(''.join(result))

