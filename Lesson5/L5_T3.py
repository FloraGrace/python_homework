'''Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32'''

with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    data_dict = {line.split()[0]: float(line.split()[1]) for line in my_file.readlines()} #создаем словарь: ключ = Фамилия, значение = оклад

sum = 0
dict_filtr = {}
#print(f"{'='* 50}\n Список всех сотрудников с окладами:")
for surname, salary in data_dict.items():  # перебор словаря: ключ = surname, значение = salary
#    print(surname, "-", salary)
    sum += salary
    if salary < 20000:
        dict_filtr[surname] = salary
try:
    average_salary = sum / len(data_dict)
except ZeroDivisionError:
    print('Деление на 0')

print(f"{'='* 50}\n Средняя величина дохода сотрудников -  {round(average_salary, 2)}\n{'='* 50}\n "
      f"Список сотрудников с окладом меньше 20 000.00")
for surname, salary in dict_filtr.items():
    print(surname, '-', salary)
