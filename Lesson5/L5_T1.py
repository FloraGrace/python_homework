'''Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.'''

with open('L5_T1.txt', 'w') as my_file:
    while True:
        line = input('Введите данные: ')
        if line == '':
            break
        else:
            my_file.writelines(line + '\n')

# проверка записанного файла
with open('L5_T1.txt', 'r') as my_file:
    my_file_reade = my_file.read()
    print(my_file_reade)
