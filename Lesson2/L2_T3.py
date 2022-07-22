''' 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
'''
while True:
    user_month = input('Введите номер месяца: ')
    key_season = int(user_month) // 3
    if user_month.isdigit() and 1<= int(user_month) <= 12:
        list_season = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
        dict_season = {0:'Зима', 1:'Весна', 2:'Лето', 3:'Осень', 4:'Зима'}
        print(f'Список сезонов - {list_season[key_season]}')
        print(f'Словарь сезонов - {dict_season[key_season]}')
        break
    else:
        print('Ошибка ввода номера месяца')