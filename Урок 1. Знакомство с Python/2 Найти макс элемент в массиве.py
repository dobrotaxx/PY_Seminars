lst = [1, 20, 5, 6, 8]
max = lst[0]

for i in range(1,len(lst)): # range от первого элемента до длины списка
    if lst[i] > max:
        max = lst[i]
print(f'Максимальное число {max}')