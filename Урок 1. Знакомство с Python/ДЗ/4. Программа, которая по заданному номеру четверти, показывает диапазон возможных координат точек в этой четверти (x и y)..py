# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
def inputInt(prompt=None):
    while True:
        usersNum = input(prompt)
        try:
            return int(usersNum)
        except ValueError:
            print(f'Вы ввели {usersNum}. Ожидалось число от 1 до 4.')

def CheckOfQuarter(usersQuarter = None):
    if usersQuarter == 1:
        print('Диапазон возможных координат [x>0,y>0]')
    elif usersQuarter == 2:
        print('Диапазон возможных координат [x<0,y>0]')
    elif usersQuarter == 3:
        print('Диапазон возможных координат [x<0,y<0]')
    elif usersQuarter == 4:
        print('Диапазон возможных координат [x>0,y<0]')

usersQuarter = inputInt('Введите номер четверти цифрами от 1 до 4: ')

while usersQuarter < 1 or usersQuarter > 4:
    print(f'Вы ввели {usersQuarter}. Ожидалось число от 1 до 4.')
    usersQuarter = inputInt('Введите номер четверти цифрами от 1 до 4: ')

result = CheckOfQuarter(usersQuarter)


