"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property."""

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure

class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def expenditure(self):
        return round(self.size / 6.5 + 0.5, 2)

class Suit(Clothes):

    def __init__(self, name, length):
        super().__init__(name)
        self.length = length / 100 #решила рост перевести в метры, т.к. считаю, что в формулах метры.

    @property
    def expenditure(self):
        return round((2 * self.length + 0.3), 2)

coat = Coat('Пальто зимнее', 48)
suit = Suit('Костюм чёрный', 178)


print(f'Для {coat.name} размер {coat.size}, потребуется ткани {coat.expenditure}')
print(f'Для {suit.name} размер {suit.length}, потребуется ткани {suit.expenditure}')
print(f'Общий расход ткани одежды {coat + suit}')
