'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.'''

class MyExceptionZero(Exception):
    pass

while True:
    try:

        a = input('Введите делимое или любой символ, кроме цифры для завершения ')
        if not a.isdigit():
            break
        b = input('Введите делитель ')
        a, b = int(a), int(b)
        if b == 0:
            raise MyExceptionZero("Делить на 0 нельзя!")

    except MyExceptionZero as err:
        print(err)
    else:
        print(f"{round(a / b, 2)}")

####### Вариант2 ################

# class MyExceptionZero(Exception):
#     pass
#
# try:
#     a = int(input('Введите делимое  '))
#     b = int(input('Введите делитель '))
#     if b == 0:
#         raise MyExceptionZero("Делить на 0 нельзя!")
#
# except MyExceptionZero as err:
#     print(err)
# else:
#     print(f"{round(a / b, 2)}")
