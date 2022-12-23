# 2. Создайте программу для игры в ""Крестики-нолики"".

from random import randint
import random
# from itertools import count

def check_win(itsO,itsX):

    for e in range(1, 3):
        o = 0
        x = 0
        for j in range(2, 6, 2):
            if field[e][j] == 'O':
                o += 1
            if field[e][j] == 'X':
                x += 1
            if o == int(itsO) and x == int(itsX) and players[i] == 'O':
                for j in range(2, 3, 2):
                    if field[e][j] == ' ':
                        field[e][j] = players[i]

            elif o == int(itsX) and x == int(itsO) and players[i] == 'X':
                for j in range(2, 3, 2):
                    if field[e][j] == ' ':
                        field[e][j] = players[i]


    for j in range(2, 6, 2):
        o = 0
        x = 0
        for e in range(1, 3):
            if field[e][j] == 'O':
                o += 1
            if field[e][j] == 'X':
                x += 1
            if o == int(itsO) and x == int(itsX) and players[i] == 'O':
                for e in range(1, 3):
                    if field[e][j] == ' ':
                        field[e][j] = players[i]
            elif o == int(itsX) and x == int(itsO) and players[i] == 'X':
                for e in range(1, 3):
                    if field[e][j] == ' ':
                        field[e][j] = players[i]
    e = 1
    o = 0
    x = 0
    j = 2
    while e < 3:
        if field[e][j] == 'O':
            o += 1
        if field[e][j] == 'X':
            x += 1
        if o == int(itsO) and x == int(itsX) and players[i] == 'O':
            d = 1
            z = 2
            while d < 3:
                if field[e][j] == ' ':
                    field[e][j] = players[i]
                z += 2
                d += 1
        elif o == int(itsX) and x == int(itsO) and players[i] == 'X':
            d = 1
            z = 2
            while d < 3:
                if field[e][j] == ' ':
                    field[e][j] = players[i]
                z += 2
                d += 1
        j += 2
        e += 1

    e = 3
    o = 0
    x = 0
    j = 2
    while e > 0:
        if field[e][j] == 'O':
            o += 1
        if field[e][j] == 'X':
            x += 1
        if o == int(itsO) and x == int(itsX) and players[i] == 'O':
            d = 3
            z = 2
            while d > 0:
                if field[e][j] == ' ':
                    field[e][j] = players[i]
                z += 2
                d -= 1
        elif o == int(itsX) and x == int(itsO) and players[i] == 'X':
            d = 3
            z = 2
            while d > 0:
                if field[e][j] == ' ':
                    field[e][j] = players[i]
                z += 2
                d -= 1

        j += 2
        e -= 1

while True:
    while True:
        mode = input('Выберите режим. '
                     '\n 1 - Игра против человека. '
                     '\n 2 - Игра против бота. '
                     '\n 3 - Умный бот. '
                     '\n Ваш выбор: ')
        if mode == str(1):
            print('\nВы выбрали режим "Игра против человека"')
            break
        elif mode == str(2):
            print('\nВы выбрали режим "Игра против бота"')
            break
        elif mode == str(3):
            print('\nВы выбрали режим "Умный бот"')
            break
        else:
            print(f'Вы ввели "{mode}". Попробуйте ещё раз.')

    print('\n Правила игры Крестики vs Нолики:'
          '\n Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).'
          '\n Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. '
          '\n Первый ход делает игрок, ставящий крестики.'
          '\n Для того, чтобы поставить фигуру в ячейку, нужно ввести в консоль индекс фигуры.'
          '\n Пример: A1, B3, C2.\n')

    i = randint(0, 1)
    players = [0, 1]

    if mode == str(1):
        x = 0
        j = 0
        field = [
            [' ', '|', 'A', '|', 'B', '|', 'C', '|'],
            ['1', '|', ' ', '|', ' ', '|', ' ', '|'],
            ['2', '|', ' ', '|', ' ', '|', ' ', '|'],
            ['3', '|', ' ', '|', ' ', '|', ' ', '|']]
        dict1 = {'Клетка А1': field[1][2], 'Клетка А2': field[2][2], 'Клетка А3': field[3][2],
                 'Клетка B1': field[1][4], 'Клетка B2': field[2][4], 'Клетка B3': field[3][4],
                 'Клетка C1': field[1][6], 'Клетка C2': field[2][6], 'Клетка C3': field[3][6]}
        for x in field:
            print(''.join(map(str, x)))
        input('\n Нажмите Enter для продолжения')
        print(f'\n Жеребьевкой выбран Игрок {i + 1}')
        players = {0: 'X', 1: 'O'}
        if i == 1:
            players = {1: 'X', 0: 'O'}
        count = 0
        while count <= 9:
            while True:
                step = input(f'\n Игрок {i + 1} "{players[i]}", Ваш ход: ')

                if step.lower() == 'a1' or step.lower() == 'ф1':
                    if field[1][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'a2' or step.lower() == 'ф2':
                    if field[2][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'a3' or step.lower() == 'ф3':
                    if field[3][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b1' or step.lower() == 'и1':
                    if field[1][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b2' or step.lower() == 'и2':
                    if field[2][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b3' or step.lower() == 'и3':
                    if field[3][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c1' or step.lower() == 'с1':
                    if field[1][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c2' or step.lower() == 'с2':
                    if field[2][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c3' or step.lower() == 'с3':
                    if field[3][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break
                else:
                    print(f'Вы ввели "{step}". Попробуйте ещё раз.')
            count += 1

            if field[1][2] == 'X' and field[2][2] == 'X' and field[3][2] == 'X' \
                    or field[1][4] == 'X' and field[2][4] == 'X' and field[3][4] == 'X' \
                    or field[1][6] == 'X' and field[2][6] == 'X' and field[3][6] == 'X' \
                    or field[1][2] == 'X' and field[1][4] == 'X' and field[1][6] == 'X' \
                    or field[2][2] == 'X' and field[2][4] == 'X' and field[2][6] == 'X' \
                    or field[3][2] == 'X' and field[3][4] == 'X' and field[3][6] == 'X' \
                    or field[1][2] == 'X' and field[2][4] == 'X' and field[3][6] == 'X' \
                    or field[1][6] == 'X' and field[2][4] == 'X' and field[3][2] == 'X':
                print(f'\nПобедил Игрок {i + 1} "{players[i]}". Поздравляем!')
                break

            elif field[1][2] == 'O' and field[2][2] == 'O' and field[3][2] == 'O' \
                    or field[1][4] == 'O' and field[2][4] == 'O' and field[3][4] == 'O' \
                    or field[1][6] == 'O' and field[2][6] == 'O' and field[3][6] == 'O' \
                    or field[1][2] == 'O' and field[1][4] == 'O' and field[1][6] == 'O' \
                    or field[2][2] == 'O' and field[2][4] == 'O' and field[2][6] == 'O' \
                    or field[3][2] == 'O' and field[3][4] == 'O' and field[3][6] == 'O' \
                    or field[1][2] == 'O' and field[2][4] == 'O' and field[3][6] == 'O' \
                    or field[1][6] == 'O' and field[2][4] == 'O' and field[3][2] == 'O':
                print(f'\nПобедил Игрок {i + 1} "{players[i]}". Поздравляем!')
                break
            elif count == 9:
                print('\nНичья!')
                break
            if i == 1:
                i -= 1
            else:
                i += 1
        while True:
            new_game = input('\n Хотите сыграть ещё раз?'
                             '\n Введите Y или N: ')
            if new_game.lower() == 'n' or new_game.lower() == 'т':
                print('Очень жаль. До встречи в следующий раз!')
                break
            elif new_game == 'y' or new_game == 'н':
                break
            else:
                print(f'Вы ввели {new_game}. Попробуйте ещё раз.')
        if new_game.lower() == 'n' or new_game.lower() == 'т':
            break
        elif new_game == 'y' or new_game == 'н':
            print()

    if mode == str(2):
        x = 0
        j = 0
        field = [
            [' ', '|', 'A', '|', 'B', '|', 'C', '|'],
            ['1', '|', ' ', '|', ' ', '|', ' ', '|'],
            ['2', '|', ' ', '|', ' ', '|', ' ', '|'],
            ['3', '|', ' ', '|', ' ', '|', ' ', '|']]
        dict1 = {'Клетка А1': field[1][2], 'Клетка А2': field[2][2], 'Клетка А3': field[3][2],
                 'Клетка B1': field[1][4], 'Клетка B2': field[2][4], 'Клетка B3': field[3][4],
                 'Клетка C1': field[1][6], 'Клетка C2': field[2][6], 'Клетка C3': field[3][6]}
        for x in field:
            print(''.join(map(str, x)))
        input('\n Нажмите Enter для продолжения')
        print(f'\n Жеребьевкой выбран Игрок {i + 1}')
        players = {0: 'X', 1: 'O'}
        if i == 1:
            players = {1: 'X', 0: 'O'}
        count = 0
        while count <= 9:
            while True:
                step = ''
                if i == 1:
                    print(f'\n Ходит Компьютер "{players[i]}": ')
                    while True:
                        line = randint(1, 3)
                        column = random.randrange(2, 7, 2)
                        if field[line][column] == " ":
                            field[line][column] = players[i]
                            for x in field:
                                print(''.join(map(str, x)))
                            break
                    break
                else:
                    step = input(f'\n Игрок {i + 1} "{players[i]}", Ваш ход: ')

                if step.lower() == 'a1' or step.lower() == 'ф1':
                    if field[1][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'a2' or step.lower() == 'ф2':
                    if field[2][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'a3' or step.lower() == 'ф3':
                    if field[3][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b1' or step.lower() == 'и1':
                    if field[1][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b2' or step.lower() == 'и2':
                    if field[2][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b3' or step.lower() == 'и3':
                    if field[3][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c1' or step.lower() == 'с1':
                    if field[1][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c2' or step.lower() == 'с2':
                    if field[2][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c3' or step.lower() == 'с3':
                    if field[3][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break
                else:
                    print(f'Вы ввели "{step}". Попробуйте ещё раз.')
            count += 1

            if field[1][2] == 'X' and field[2][2] == 'X' and field[3][2] == 'X' and i == 0 \
                    or field[1][4] == 'X' and field[2][4] == 'X' and field[3][4] == 'X' and i == 0 \
                    or field[1][6] == 'X' and field[2][6] == 'X' and field[3][6] == 'X' and i == 0 \
                    or field[1][2] == 'X' and field[1][4] == 'X' and field[1][6] == 'X' and i == 0 \
                    or field[2][2] == 'X' and field[2][4] == 'X' and field[2][6] == 'X' and i == 0 \
                    or field[3][2] == 'X' and field[3][4] == 'X' and field[3][6] == 'X' and i == 0 \
                    or field[1][2] == 'X' and field[2][4] == 'X' and field[3][6] == 'X' and i == 0 \
                    or field[1][6] == 'X' and field[2][4] == 'X' and field[3][2] == 'X' and i == 0:
                print(f'\nПобедил Игрок {i + 1} "{players[i]}". Поздравляем!')
                break

            elif field[1][2] == 'O' and field[2][2] == 'O' and field[3][2] == 'O' and i == 0 \
                    or field[1][4] == 'O' and field[2][4] == 'O' and field[3][4] == 'O' and i == 0 \
                    or field[1][6] == 'O' and field[2][6] == 'O' and field[3][6] == 'O' and i == 0 \
                    or field[1][2] == 'O' and field[1][4] == 'O' and field[1][6] == 'O' and i == 0 \
                    or field[2][2] == 'O' and field[2][4] == 'O' and field[2][6] == 'O' and i == 0 \
                    or field[3][2] == 'O' and field[3][4] == 'O' and field[3][6] == 'O' and i == 0 \
                    or field[1][2] == 'O' and field[2][4] == 'O' and field[3][6] == 'O' and i == 0 \
                    or field[1][6] == 'O' and field[2][4] == 'O' and field[3][2] == 'O' and i == 0:
                print(f'\nПобедил Игрок {i + 1} "{players[i]}". Поздравляем!')
                break

            elif field[1][2] == 'X' and field[2][2] == 'X' and field[3][2] == 'X' and i == 1 \
                    or field[1][4] == 'X' and field[2][4] == 'X' and field[3][4] == 'X' and i == 1 \
                    or field[1][6] == 'X' and field[2][6] == 'X' and field[3][6] == 'X' and i == 1 \
                    or field[1][2] == 'X' and field[1][4] == 'X' and field[1][6] == 'X' and i == 1 \
                    or field[2][2] == 'X' and field[2][4] == 'X' and field[2][6] == 'X' and i == 1 \
                    or field[3][2] == 'X' and field[3][4] == 'X' and field[3][6] == 'X' and i == 1 \
                    or field[1][2] == 'X' and field[2][4] == 'X' and field[3][6] == 'X' and i == 1 \
                    or field[1][6] == 'X' and field[2][4] == 'X' and field[3][2] == 'X' and i == 1:
                print(f'\nПобедила бездушная машина. Увы. В следующий раз Вам точно повезёт!')
                break

            elif field[1][2] == 'O' and field[2][2] == 'O' and field[3][2] == 'O' and i == 1 \
                    or field[1][4] == 'O' and field[2][4] == 'O' and field[3][4] == 'O' and i == 1 \
                    or field[1][6] == 'O' and field[2][6] == 'O' and field[3][6] == 'O' and i == 1 \
                    or field[1][2] == 'O' and field[1][4] == 'O' and field[1][6] == 'O' and i == 1 \
                    or field[2][2] == 'O' and field[2][4] == 'O' and field[2][6] == 'O' and i == 1 \
                    or field[3][2] == 'O' and field[3][4] == 'O' and field[3][6] == 'O' and i == 1 \
                    or field[1][2] == 'O' and field[2][4] == 'O' and field[3][6] == 'O' and i == 1 \
                    or field[1][6] == 'O' and field[2][4] == 'O' and field[3][2] == 'O' and i == 1:
                print(f'\nПобедила бездушная машина. Увы. В следующий раз Вам точно повезёт!')
                break
            elif count == 9:
                print('\nНичья!')
                break
            if i == 1:
                i -= 1
            else:
                i += 1
        while True:
            new_game = input('\n Хотите сыграть ещё раз?'
                             '\n Введите Y или N: ')
            if new_game.lower() == 'n' or new_game.lower() == 'т':
                print('Очень жаль. До встречи в следующий раз!')
                break
            elif new_game == 'y' or new_game == 'н':
                break
            else:
                print(f'Вы ввели {new_game}. Попробуйте ещё раз.')
        if new_game.lower() == 'n' or new_game.lower() == 'т':
            break
        elif new_game == 'y' or new_game == 'н':
            print()

    if mode == str(3):
        x = 0
        j = 0
        field = [
            ['№', '|', 'A', '|', 'B', '|', 'C', '|'],
            ['1', '|', ' ', '|', ' ', '|', ' ', '|'],
            ['2', '|', ' ', '|', ' ', '|', ' ', '|'],
            ['3', '|', ' ', '|', ' ', '|', ' ', '|']]
        # dict1 = {'Клетка А1': field[1][2], 'Клетка А2': field[2][2], 'Клетка А3': field[3][2],
        #          'Клетка B1': field[1][4], 'Клетка B2': field[2][4], 'Клетка B3': field[3][4],
        #          'Клетка C1': field[1][6], 'Клетка C2': field[2][6], 'Клетка C3': field[3][6]}
        # victories = [[field[1][2], field[1][4], field[1][6]],
        #              [field[2][2], field[2][4], field[2][6]],
        #              [field[3][2], field[3][4], field[3][6]],
        #              [field[1][2], field[2][2], field[3][2]],
        #              [field[1][4], field[2][4], field[3][4]],
        #              [field[1][6], field[2][6], field[3][6]],
        #              [field[1][2], field[2][4], field[3][6]],
        #              [field[1][6], field[2][4], field[3][2]]]

        for x in field:
            print(''.join(map(str, x)))
        input('\n Нажмите Enter для продолжения')
        print(f'\n Жеребьевкой выбран Игрок {i + 1}')
        players = {0: 'X', 1: 'O'}
        if i == 1:
            players = {1: 'X', 0: 'O'}
        count = 0
        while count <= 9:
            step = ''
            while True:
                if i == 1:
                    print(f'\n Ходит Компьютер "{players[i]}": ')
                    while True:
                        check_win(2, 0)
                        check_win(0, 2)
                        check_win(1, 0)
                        if field[2][4] == ' ':
                            field[2][4] = players[i]
                            for x in field:
                                print(''.join(map(str, x)))
                            break
                        else:
                            if field[1][2] == ' ':
                                field[1][2] = players[i]
                            for e in range(1, len(field)):
                                for j in range(2, len(field), 2):
                                    if field[e][j] == ' ':
                                        field[e][j] = players[i]
                                        for x in field:
                                            print(''.join(map(str, x)))

                    break
                else:
                    step = input(f'\n Игрок {i + 1} "{players[i]}", Ваш ход: ')

                if step.lower() == 'a1' or step.lower() == 'ф1':
                    if field[1][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'a2' or step.lower() == 'ф2':
                    if field[2][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'a3' or step.lower() == 'ф3':
                    if field[3][2] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][2] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b1' or step.lower() == 'и1':
                    if field[1][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b2' or step.lower() == 'и2':
                    if field[2][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'b3' or step.lower() == 'и3':
                    if field[3][4] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][4] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c1' or step.lower() == 'с1':
                    if field[1][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[1][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c2' or step.lower() == 'с2':
                    if field[2][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[2][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break

                elif step.lower() == 'c3' or step.lower() == 'с3':
                    if field[3][6] != ' ':
                        print('Эта клетка уже занята. Попробуйте ещё раз.')
                    else:
                        field[3][6] = players[i]
                        for x in field:
                            print(''.join(map(str, x)))
                        break
                else:
                    print(f'Вы ввели "{step}". Попробуйте ещё раз.')
            count += 1

            if field[1][2] == 'X' and field[2][2] == 'X' and field[3][2] == 'X' and i == 0 \
                    or field[1][4] == 'X' and field[2][4] == 'X' and field[3][4] == 'X' and i == 0 \
                    or field[1][6] == 'X' and field[2][6] == 'X' and field[3][6] == 'X' and i == 0 \
                    or field[1][2] == 'X' and field[1][4] == 'X' and field[1][6] == 'X' and i == 0 \
                    or field[2][2] == 'X' and field[2][4] == 'X' and field[2][6] == 'X' and i == 0 \
                    or field[3][2] == 'X' and field[3][4] == 'X' and field[3][6] == 'X' and i == 0 \
                    or field[1][2] == 'X' and field[2][4] == 'X' and field[3][6] == 'X' and i == 0 \
                    or field[1][6] == 'X' and field[2][4] == 'X' and field[3][2] == 'X' and i == 0:
                print(f'\nПобедил Игрок {i + 1} "{players[i]}". Поздравляем!')
                break

            elif field[1][2] == 'O' and field[2][2] == 'O' and field[3][2] == 'O' and i == 0 \
                    or field[1][4] == 'O' and field[2][4] == 'O' and field[3][4] == 'O' and i == 0 \
                    or field[1][6] == 'O' and field[2][6] == 'O' and field[3][6] == 'O' and i == 0 \
                    or field[1][2] == 'O' and field[1][4] == 'O' and field[1][6] == 'O' and i == 0 \
                    or field[2][2] == 'O' and field[2][4] == 'O' and field[2][6] == 'O' and i == 0 \
                    or field[3][2] == 'O' and field[3][4] == 'O' and field[3][6] == 'O' and i == 0 \
                    or field[1][2] == 'O' and field[2][4] == 'O' and field[3][6] == 'O' and i == 0 \
                    or field[1][6] == 'O' and field[2][4] == 'O' and field[3][2] == 'O' and i == 0:
                print(f'\nПобедил Игрок {i + 1} "{players[i]}". Поздравляем!')
                break

            elif field[1][2] == 'X' and field[2][2] == 'X' and field[3][2] == 'X' and i == 1 \
                    or field[1][4] == 'X' and field[2][4] == 'X' and field[3][4] == 'X' and i == 1 \
                    or field[1][6] == 'X' and field[2][6] == 'X' and field[3][6] == 'X' and i == 1 \
                    or field[1][2] == 'X' and field[1][4] == 'X' and field[1][6] == 'X' and i == 1 \
                    or field[2][2] == 'X' and field[2][4] == 'X' and field[2][6] == 'X' and i == 1 \
                    or field[3][2] == 'X' and field[3][4] == 'X' and field[3][6] == 'X' and i == 1 \
                    or field[1][2] == 'X' and field[2][4] == 'X' and field[3][6] == 'X' and i == 1 \
                    or field[1][6] == 'X' and field[2][4] == 'X' and field[3][2] == 'X' and i == 1:
                print(f'\nПобедила бездушная машина. Увы. В следующий раз Вам точно повезёт!')
                break

            elif field[1][2] == 'O' and field[2][2] == 'O' and field[3][2] == 'O' and i == 1 \
                    or field[1][4] == 'O' and field[2][4] == 'O' and field[3][4] == 'O' and i == 1 \
                    or field[1][6] == 'O' and field[2][6] == 'O' and field[3][6] == 'O' and i == 1 \
                    or field[1][2] == 'O' and field[1][4] == 'O' and field[1][6] == 'O' and i == 1 \
                    or field[2][2] == 'O' and field[2][4] == 'O' and field[2][6] == 'O' and i == 1 \
                    or field[3][2] == 'O' and field[3][4] == 'O' and field[3][6] == 'O' and i == 1 \
                    or field[1][2] == 'O' and field[2][4] == 'O' and field[3][6] == 'O' and i == 1 \
                    or field[1][6] == 'O' and field[2][4] == 'O' and field[3][2] == 'O' and i == 1:
                print(f'\nПобедила бездушная машина. Увы. В следующий раз Вам точно повезёт!')
                break
            elif count == 9:
                print('\nНичья!')
                break
            if i == 1:
                i -= 1
            else:
                i += 1
        while True:
            new_game = input('\n Хотите сыграть ещё раз?'
                             '\n Введите Y или N: ')
            if new_game.lower() == 'n' or new_game.lower() == 'т':
                print('Очень жаль. До встречи в следующий раз!')
                break
            elif new_game == 'y' or new_game == 'н':
                break
            else:
                print(f'Вы ввели {new_game}. Попробуйте ещё раз.')
        if new_game.lower() == 'n' or new_game.lower() == 'т':
            break
        elif new_game == 'y' or new_game == 'н':
            print()
