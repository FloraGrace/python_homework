'''Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''

class ComplexNumbe():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return complex((self.x * other.x - self.y * other.y), (self.x * other.y + other.x * self.y)) #(x1 * x2 - y1 * y2) + (x1 * y2 + x2 * y1)*i

    def __add__(self, other):
        return complex((self.x + other.x), (self.y + other.y))

c = ComplexNumbe(1, 2)
d = ComplexNumbe(3, 4)
print(f'Сумма {complex(c.x, c.y)} и {complex(d.x, d.y)} равна {c + d}')
print(f'Произведение {complex(c.x, c.y)} и {complex(d.x, d.y)} равна {c * d}')
