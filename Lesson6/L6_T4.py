'''Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.'''

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        if direction == 0:
            return f'Машина {self.name} {self.color} повернула направо'
        else:
            return f'Машина {self.name} {self.color} повернула налево'

    def show_speed(self):
        return f'Скорость машины {self.name} - {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'У машины {self.name} превышение скорости и равна {self.speed}'
        else:
            return f'Скорость машины {self.name} - {self.speed}'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'У машины {self.name} превышение скорости и равна {self.speed}'
        else:
            return f'Скорость машины {self.name} - {self.speed}'

class PoliceCar(Car):
    
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

viper = SportCar(200, 'Красный', 'Dodge Viper', False)
matiz = TownCar(61, 'Жёлтый', 'Daewoo Matiz', False)
matiz_2 = TownCar(30, 'Хамелион', 'Daewoo Matiz', False)
lada = WorkCar(80, 'Белая', 'Лада Ларгус', False)
fiat = PoliceCar(60, 'Бело-синяя', 'Fiat Ducato Combi', True)

print(lada.turn(1))
print(f'{"Полицеская машина" if viper.is_police == True else "Не полицейская машина"} '
      f'{viper.name}, цвет {viper.color}, движется со скоростью {viper.speed}км\ч')
print(lada.turn(0))
print(matiz.show_speed())
print(lada.show_speed())
print(f'{matiz_2.show_speed()} и {matiz_2.go()}')
print(f'{"Полицеская машина" if fiat.is_police == True else "Не полицейская машина"} '
      f'{fiat.name}, цвет {fiat.color}, движется со скоростью {fiat.speed}км\ч')
print(matiz_2.stop())
print(f'{"Полицеская машина" if lada.is_police == True else "Не полицейская машина"} '
      f'{lada.name}, цвет {lada.color}, движется со скоростью {lada.speed}км\ч')
