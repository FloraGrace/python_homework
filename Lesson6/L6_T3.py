'''Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.'''

class Worker:

    # атрибуты класса
    name = ()
    surname = None
    position = None
    _income = {'wage': 0, 'bonus': 0}

    # методы класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'Полное имя сотрудника - {self.name} {self.surname}'

    def get_full_profit(self):
        return f'Доход - {sum(self._income.values())}'

conclusion = Position('Иван', 'Петров', 'машинист', 15000, 20000)

print(f'Имя - {conclusion.name}\n Фамилия -{conclusion.surname}\n '
      f'должность - {conclusion.position}\n оклад - {conclusion._income.get("wage")}\n '
      f'бонус - {conclusion._income.get("bonus")}')
print(conclusion.get_full_name())
print(conclusion.get_full_profit())