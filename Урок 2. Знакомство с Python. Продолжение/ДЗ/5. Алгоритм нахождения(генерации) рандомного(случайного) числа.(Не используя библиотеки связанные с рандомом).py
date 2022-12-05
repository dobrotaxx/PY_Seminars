# 5. Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
# (Не используя библиотеки связанные с рандомом)

import time

start = int(input('Нижний предел')
end = int(input('Верхний предел')
random_number = int((time.time() % 1) * (end - start) + start)
print(f'Случайное число в диапазоне от {start} до {end}: {random_number}')
