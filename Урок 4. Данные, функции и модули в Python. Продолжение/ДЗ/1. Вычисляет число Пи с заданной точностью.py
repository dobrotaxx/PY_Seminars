# 1. Вычислить число Пи c заданной точностью d
# Пример:
#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10
numP = list(str(3.1415926535))
accuracyOfUser = str(input('Задайте точность для числа Пи: '))
while len(numP) != len(accuracyOfUser):
    numP.pop()
print(''.join(map(str,numP)))
