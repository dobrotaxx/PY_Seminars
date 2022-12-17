# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
from itertools import count


def Declination_check(n, msg1, msg2, msg3, msg4):
    if n in (11, 12, 13, 14):
        print(msg1)
    elif n % 10 == 1:
        print(msg2)
    elif n % 10 in (2, 3, 4):
        print(msg3)
    else:
        print(msg4)


def Volume_of_sweets(msg='Укажите количество конфет: '):
    while True:
        try:
            volume_of_sweets = int(input(msg))
            if volume_of_sweets <= 0:
                print('Вы ввели число меньше или равное 0. Попробуйте ещё раз.')
            else:
                break
        except:
            print(f'Вы ввели не число. Попробуйте ещё раз.')
    Declination_check(volume_of_sweets,
                      f'Правила игры:'
                      f'\n На столе лежит {volume_of_sweets} конфет.'
                      f'\n Играют два игрока делая ход друг после друга.'
                      f'\n Первый ход определяется жеребьёвкой.'
                      f'\n За один ход можно забрать не более чем 28 конфет.'
                      f'\n Все конфеты оппонента достаются сделавшему последний ход.',
                      f'Правила игры:'
                      f'\n На столе лежит {volume_of_sweets} конфета.'
                      f'\n Играют два игрока делая ход друг после друга.'
                      f'\n Первый ход определяется жеребьёвкой.'
                      f'\n За один ход можно забрать не более чем 28 конфет.'
                      f'\n Все конфеты оппонента достаются сделавшему последний ход.',
                      f'Правила игры:'
                      f'\n На столе лежит {volume_of_sweets} конфеты.'
                      f'\n Играют два игрока делая ход друг после друга.'
                      f'\n Первый ход определяется жеребьёвкой.'
                      f'\n За один ход можно забрать не более чем 28 конфет.'
                      f'\n Все конфеты оппонента достаются сделавшему последний ход.',
                      f'Правила игры:'
                      f'\n На столе лежит {volume_of_sweets} конфет.'
                      f'\n Играют два игрока делая ход друг после друга.'
                      f'\n Первый ход определяется жеребьёвкой.'
                      f'\n За один ход можно забрать не более чем 28 конфет.'
                      f'\n Все конфеты оппонента достаются сделавшему последний ход.')
    return volume_of_sweets


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
            print(f'Вы ввели {mode}. Попробуйте ещё раз.')

    volume_of_sweets = Volume_of_sweets()

    i = randint(0, 1)
    players = [0, 1]
    if mode == str(1):
        input('\n Нажмите Enter для продолжения')
        print(f'\n Жеребьевкой выбран игрок {i + 1}')
        while volume_of_sweets != 0:
            while True:
                try:
                    players[i] = int(input(f'\n Игрок {i + 1}, Ваш ход: '))
                    if players[i] >= 1 and players[i] <= 28 and players[i] <= volume_of_sweets:
                        Declination_check(players[i],
                                          f'    Игрок {i + 1} взял {players[i]} конфет.',
                                          f'    Игрок {i + 1} взял {players[i]} конфету.',
                                          f'    Игрок {i + 1} взял {players[i]} конфеты.',
                                          f'    Игрок {i + 1} взял {players[i]} конфет.')
                        break
                    elif players[i] > 28:
                        print('Нельзя брать больше 28! Попробуйте ещё раз.')
                    elif players[i] > volume_of_sweets and players[i] <= 28:
                        print(f'Вы пытаетесь взять больше, чем осталось. Попробуйте ещё раз.')
                except ValueError:
                    print(f'Вы ввели не число. Попробуйте ещё раз.')
            volume_of_sweets -= players[i]
            Declination_check(volume_of_sweets,
                              f'    Осталось {volume_of_sweets} конфет.',
                              f'    Осталась {volume_of_sweets} конфета.',
                              f'    Осталось {volume_of_sweets} конфеты.',
                              f'    Осталось {volume_of_sweets} конфет.')
            if volume_of_sweets <= 0:
                print(f'Победил Игрок {i + 1}. Все конфеты достаются ему. Поздравляем!')
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
        input('\n Нажмите Enter для продолжения')
        print(f'\n Жеребьевкой выбран игрок {i + 1}')
        while volume_of_sweets != 0:
            while True:
                if i == 1:
                    print('\n Ходит Игрок 2: ')
                    if volume_of_sweets > 28:
                        players[i] = randint(1, 28)
                    else:
                        players[i] = randint(1, volume_of_sweets)
                    Declination_check(players[i],
                                      f'    Игрок {i + 1} взял {players[i]} конфет.',
                                      f'    Игрок {i + 1} взял {players[i]} конфету.',
                                      f'    Игрок {i + 1} взял {players[i]} конфеты.',
                                      f'    Игрок {i + 1} взял {players[i]} конфет.')
                    break
                try:
                    players[i] = int(input(f'\n Игрок {i + 1}, Ваш ход: '))
                    if players[i] >= 1 and players[i] <= 28 and players[i] <= volume_of_sweets:
                        Declination_check(players[i],
                                          f'    Игрок {i + 1} взял {players[i]} конфет.',
                                          f'    Игрок {i + 1} взял {players[i]} конфету.',
                                          f'    Игрок {i + 1} взял {players[i]} конфеты.',
                                          f'    Игрок {i + 1} взял {players[i]} конфет.')
                        break
                    elif players[i] > 28:
                        print('Нельзя брать больше 28! Попробуйте ещё раз.')
                    elif players[i] > volume_of_sweets and players[i] <= 28:
                        print(f'Вы пытаетесь взять больше, чем осталось. Попробуйте ещё раз.')
                except ValueError:
                    print(f'Вы ввели не число. Попробуйте ещё раз.')
            volume_of_sweets -= players[i]
            Declination_check(volume_of_sweets,
                              f'    Осталось {volume_of_sweets} конфет.',
                              f'    Осталась {volume_of_sweets} конфета.',
                              f'    Осталось {volume_of_sweets} конфеты.',
                              f'    Осталось {volume_of_sweets} конфет.')
            if volume_of_sweets <= 0:
                print(f'Победил Игрок {i + 1}. Все конфеты достаются ему. Поздравляем!')
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
        input('\n Нажмите Enter для продолжения')
        print(f'\n Жеребьевкой выбран игрок {i + 1}')
        while volume_of_sweets != 0:
            while True:
                if i == 1:
                    print('\n Ходит Игрок 2: ')
                    if volume_of_sweets <= 28:
                        players[i] = volume_of_sweets
                    elif volume_of_sweets > 28:
                        players[i] = volume_of_sweets % 29
                        if players[i] == 0:
                            players[i] += 1
                    else:
                        players[i] = randint(1, volume_of_sweets)
                    Declination_check(players[i],
                                      f'    Игрок {i + 1} взял {players[i]} конфет.',
                                      f'    Игрок {i + 1} взял {players[i]} конфету.',
                                      f'    Игрок {i + 1} взял {players[i]} конфеты.',
                                      f'    Игрок {i + 1} взял {players[i]} конфет.')
                    break
                try:
                    players[i] = int(input(f'\n Игрок {i + 1}, Ваш ход: '))
                    if players[i] >= 1 and players[i] <= 28 and players[i] <= volume_of_sweets:
                        Declination_check(players[i],
                                          f'    Игрок {i + 1} взял {players[i]} конфет.',
                                          f'    Игрок {i + 1} взял {players[i]} конфету.',
                                          f'    Игрок {i + 1} взял {players[i]} конфеты.',
                                          f'    Игрок {i + 1} взял {players[i]} конфет.')
                        break
                    elif players[i] > 28:
                        print('Нельзя брать больше 28! Попробуйте ещё раз.')
                    elif players[i] > volume_of_sweets and players[i] <= 28:
                        print(f'Вы пытаетесь взять больше, чем осталось. Попробуйте ещё раз.')
                except ValueError:
                    print(f'Вы ввели не число. Попробуйте ещё раз.')
            volume_of_sweets -= players[i]
            Declination_check(volume_of_sweets,
                              f'    Осталось {volume_of_sweets} конфет.',
                              f'    Осталась {volume_of_sweets} конфета.',
                              f'    Осталось {volume_of_sweets} конфеты.',
                              f'    Осталось {volume_of_sweets} конфет.')
            if volume_of_sweets <= 0:
                print(f'Победил Игрок {i + 1}. Все конфеты достаются ему. Поздравляем!')
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
