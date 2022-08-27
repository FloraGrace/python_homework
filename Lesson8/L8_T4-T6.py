'''4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый
тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.'''

class Store():

    def __init__(self, store_id, store_name, store_address, **store_dev):
        self.store_id = store_id
        self.store_name = store_name
        self.store_address = store_address
        self.store_dev = store_dev

    def store_info(self):
        print(f'\nid-склада: {self.store_id} '
              f'\nНазвание склада: {self.store_name} '
              f'\nАдрес склада: {self.store_address}')

    def check_count(self, dev_count):
        """ проверка остатков на складе"""
        ret_val = True
        for dev, count in dev_count.items():
            if dev not in self.store_dev:
                print(f'\nНа складе {self.store_name} \n Товар ({dev.id}) {dev.model_name} отсутствует !')
                ret_val = False
                break
            elif self.store_dev[dev] < count:
                print(f'\nНа складе {self.store_name} \n Товар ({dev.id}) {dev.model_name} отсутствует  в нужном количестве!')
                ret_val = False
                break
        return ret_val

    def move_dev(self, move_type, dev_count):
        if move_type == 'in': # перемещение на склад
            print(f'\nПеремещение на склад {self.store_name}:')
            for dev, count in dev_count.items():
                print(f' товара ({dev.id}) {dev.model_name}: {count} шт')
                if dev not in self.store_dev:
                    self.store_dev[dev] = count
                else:
                    self.store_dev[dev] += count
        elif move_type == 'out': # перемещение со склада
            print(f'\nПеремещение со склада {self.store_name}:')
            for dev, count in dev_count.items():
                print(f' товара ({dev.id}) {dev.model_name}: {count} шт.')
                self.store_dev[dev] -= count

    def print_dev_count(self):
        print(f'На складе {self.store_name}')
        for key, value in self.store_dev.items():
            print(f' товара ({key.id}) {key.model_name} {value} шт.')


class Devices():
    def __init__(self, id, model_name, serial_num, country):
        self.id = id                    # уникальный идентификатор
        self.model_name = model_name    # наименование модели
        self.serial_num = serial_num    # серийный номер
        self.country = country          # страна-производитель


    def info(self):
        print(f'id: {self.id} '
              f'\nНаименование модели: {self.model_name}'
              f'\nСерийный номер: {self.serial_num}'
              f'\nСтрана-производитель: {self.country}')


class Printer(Devices):
    def __init__(self, id, model_name, serial_num, country, printer_type, pps):
        self.type = 'Принтер'
        self.printer_type = printer_type    # тип печати (матричный, струйный, лазерный)
        self.pps = pps                      # скорость печати
        super().__init__(id, model_name, serial_num, country)


    def info(self):
        print(f'\nТип устройства: {self.type}'
              f'\nТип печати: {self.printer_type}'
              f'\nСкорость печати: {self.pps}')
        super().info()


class Scanner(Devices):
    def __init__(self, id, model_name, serial_num, country, scanner_type, res, pps):
        self.type = 'Сканер'
        self.scanner_type = scanner_type    # планшетный, ручной
        self.res = res                      # разрешение
        self.pps = pps                      # скорость сканирования
        super().__init__(id, model_name, serial_num, country)


    def info(self):
        print(f'\nТип устройства: {self.type}'
              f'\nТип сканера: {self.scanner_type}'
              f'\nРазрешение: {self.res}'
              f'\nСкорость сканирования: {self.pps}')
        super().info()


class Copier(Devices):
    def __init__(self, id, model_name, serial_num, country, copier_type, res, lumen):
        self.type = 'Копир'
        self.copier_type = copier_type    # LCD, DLP, LCoS
        self.res = res                          # разрешение
        self.lumen = lumen                      # световой поток
        super().__init__(id, model_name, serial_num, country)


    def info(self):
        print(f'\nТип устройства: {self.type}'
              f'\nТип проектора: {self.copier_type}'
              f'\nРазрешение: {self.res}'
              f'\nСветовой поток: {self.lumen}')
        super().info()


store_lst = []
dev_lst = []

store_lst.append(Store(1, 'Центральный склад', 'адрес ЦСк'))
store_lst.append(Store(2, 'Склад 2', 'адрес склада 2'))
store_lst.append(Store(3, 'Склад 3', 'адрес склада 3'))

print(f'\n*** Склады ***')
store_lst[0].store_info()
store_lst[1].store_info()
store_lst[2].store_info()

dev_lst.append(Copier(1, 'Копир #1', 'fgsv1234', 'China', 'LCD', '1200x1200', 50000))
dev_lst.append(Printer(2, 'Принтер #2', '12dv45w', 'China', 'laser', '16ppm'))
dev_lst.append(Scanner(3, 'Сканер #3', 'dfr3r4us', 'Japan', 'Планшетный', '1200dpi', '30сек'))
dev_lst.append(Scanner(5, 'Сканер #5', '4fr3r4us', 'China', 'Ручной', '900dpi', '12сек'))

print(f'\n*** Заполняем склады начальными остатками ***')
store_lst[0].move_dev('in', {dev_lst[0]: 2, dev_lst[1]: 4, dev_lst[2]: 5})
store_lst[1].move_dev('in', {dev_lst[0]: 1, dev_lst[1]: 1, dev_lst[2]: 1})
store_lst[2].move_dev('in', {dev_lst[2]: 1, dev_lst[3]: 2, dev_lst[1]: 1})

def check_store(store_id):
    # проверка пользовательского ввода номера склада
    store = None
    for i in store_lst:
        if i.store_id == store_id:
            store = i
            break

    return store


def print_store_list():
    for i, store in enumerate(store_lst):
        print(f'{i+1}. {store.store_name}')


def get_store(msg):
    print(msg)
    print_store_list()
    store_id = input('Введите id склада (пустую строку для отмены операции): ')

    store = None
    try:
        store_id = int(store_id)
    except ValueError:
        print('Введено не числовое значение либо пустая строка!')
    else:
        store = check_store(store_id)
        if not store:
            print('В списке складов отсутствует введенное значение!')

    return store

def get_dev_by_id(dev_id):
    # проверка пользовательского ввода id товара
    dev = None
    for i in dev_lst:
        if i.id == dev_id:
            dev = i
            break

    return dev


def parse_dev_count(store, str_dev_count):
    dev_count = {}
    store = None

    try:
        # разбиваем строку  с количеством товара на отдельные позиции
        lst1 = str_dev_count.split(',')
    except:
        print(f'Ошибка при обработке введенной строки: {str_dev_count}')
    else:
        for i in lst1:
            try:
                # разбиваем каждую позицию на id товара и количество
                parse_dev_id, parse_dev_count = i.split(' ')
                parse_dev_id = int(parse_dev_id)
                parse_dev_count = int(parse_dev_count)
            except:
                print(f'Ошибка при обработке введенной подстроки: {i}, будет проигнорирована!')
            else:
                # записываем в возвращаемый словарь из пользовательского ввода количество по каждой позиции
                dev = get_dev_by_id(parse_dev_id)
                if not dev:
                    print(f'Товар с id = {parse_dev_id} не найден в справочнике, будет проигнорирован!')
                else:
                    dev_count[dev] = parse_dev_count

    return dev_count


while True:
    from_store = None
    to_store = None
    dev_count = None

    from_store = get_store('\nДля операции перемещения товара выберите склад-источник: ')
    if not from_store:
        print('Операция отменена!')
        break

    to_store = get_store('\nВыберите склад-получатель: ')
    if not to_store:
        print('Операция отменена!')
        break

    from_store.print_dev_count()
    str_dev_count = input('Введите через запятую количество перемещаемого товара в формате: <№ товара><пробел><количество>: ')

    dev_count = parse_dev_count(from_store, str_dev_count)
    if len(dev_count) == 0:
        print('Не удалось распознать введенную строку!')
    else:
        if from_store.check_count(dev_count):
            from_store.move_dev('out', dev_count)
            to_store.move_dev('in', dev_count)
            print('Операция перемещения товара выполнена. Остатки товара на складах после перемещения:')
            from_store.print_dev_count()
            to_store.print_dev_count()
        else:
            print('Операция перемещения товаров не выполнена!')
