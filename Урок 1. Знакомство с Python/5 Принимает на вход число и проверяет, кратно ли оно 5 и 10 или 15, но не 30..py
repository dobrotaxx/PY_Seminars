num = int(input('Введите число: '))
print((num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and not num % 30 == 0)