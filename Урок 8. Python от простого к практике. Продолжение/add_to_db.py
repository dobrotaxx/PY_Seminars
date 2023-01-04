def add_to_txt(data):
    with open('phone_book.txt', 'a') as book:
        data_str = (f'Имя: {data[0]}\nФамилия: {data[1]}\nНомер телефона: {data[2]}\n')
        if len(data) > 3:
            data_str += f'Описание {data[3]}\n'
        data_str += '\n'
        book.write(data_str)
def add_to_csv(data):
    with open('phone_book.csv', 'a') as book:
        data_str = str.join(';', data) + '\n'
        book.write(data_str)