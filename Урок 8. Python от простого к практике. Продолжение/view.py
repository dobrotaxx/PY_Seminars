import time

import validate


def write_data():
    phone_record = [input('Введите имя: ').title(), input('Введите фамилию: ').title()]
    phone = ''
    while not validate.check_number(phone):
        phone = input('Введите номер телефона в формате +7XXXXXXXXXX: ')
        if not validate.check_number(phone):
            print('Телефон введен неверно. Попробуйте снова.')
    phone_record.append(phone)
    description = input('Введите описание: ')
    if description:
        phone_record.append(description)
    print(f'Запись внесена в книгу: {str.join(", ", phone_record)}')
    return phone_record

def search_data():
    return input('Введите данные для поиска: ')
def show_data(data):
    print(f'Найдено записей: {len(data)}')
    for line in data:
        print(line)

def show_ext_data(data):
    print(f'Найдено записей: {len(data)}\n')
    for line in data:
        for text in line:
            print(text)

def main_menu():
    print('---')
    time.sleep(1)
    print("Главное меню")
    mode = input('1. Добавить данные.\n2. Показать данные.\n3. Поиск записи.\n4. Выход.\nВведите 1, 2, 3 или 4: ')
    if mode in '1234':
        print('---')
        return int(mode)
    else:
        print('Ошибка ввода. Попробуйте снова. Введите 1, 2, 3 или 4: ')