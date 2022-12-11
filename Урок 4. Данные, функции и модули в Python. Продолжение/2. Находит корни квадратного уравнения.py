# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
str1 = '- 4 * x^2 + 3 * x - 8 = 0'

nums = str1.split()
nums1 = []
for i in nums:
    if i.isdigit() or i == '-':
        nums1.append(i)
    if i == '=':
        break
print(nums1)

i = 0
while nums1.count('-') != 0:
    if nums1[i] == '-':
        nums1[i] += nums1[i + 1]
        nums1.pop(i + 1)
        i = 0
    i += 1
print(nums1)

a, b, c = list(map(int, nums1))
# a, b, c = int(input('Введите число a = ')), \
#           int(input('Введите число b = ')), \
#           int(input('Введите число c = '))
Discriminant = b ** 2 - 4 * a * c
if Discriminant < 0:
    print('Корней нет')
elif Discriminant == 0:
    print(round(-b / (2 * a), 2))
else:
    print(round((-b + (Discriminant ** 0.5)) / (2 * a), 2))
    print(round((-b - (Discriminant ** 0.5)) / (2 * a), 2))
