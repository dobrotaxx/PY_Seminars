from datetime import datetime as dt

def add_to_log(data):
    time = dt.now().strftime('%d.%m.%y %H:%M:%S')
    with open('log.csv', 'a') as file:
        file.write('{};{}\n'
                   .format(time, data))