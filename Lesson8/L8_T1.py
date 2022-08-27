'''Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod.
 Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
 Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
 (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

from datetime import datetime

class MyData:

    def __init__(self, str_data):
        self.str_data = str_data

    @classmethod
    def get_data(cls, str_data):
        day, month, year = map(int, str_data.split('-'))
        return day, month, year

    @staticmethod
    def valid(str_data):
        try:
            return datetime.date(datetime.strptime(str_data, '%d-%m-%Y'))
        except ValueError:
            return 'Формат даты не верный'



data = '11-1-2022'
data_err = '12-15-2022'

my_data = MyData(data)

print(f'{my_data.str_data}')
print(f'Для даты {data} "@classmethod" =  {my_data.get_data(data)}')
print(f'Для даты {data} "@staticmethod" = {my_data.valid(data)}')
print(f'Для даты {data_err} "@staticmethod" = {my_data.valid(data_err)}')





