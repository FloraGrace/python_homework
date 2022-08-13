'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
©'''

import json

report = []
with open('text_7.txt', 'r', encoding='UTF-8') as my_file:
    text = my_file.readline()
    my_file.seek(0)
    profits = {}
    profit_sum = 0
    i = 0
    for line in my_file:
        my_line = line.split(' ')
        profit = int(my_line[2]) - int(my_line[3])
        profits.update({my_line[0]: profit})
        if profit > 0:
            profit_sum += profit
            i += 1

    report.append(profits)
    report.append({'average_profit': (profit_sum / i)})

with open('text_77.json', 'w', encoding='UTF-8') as json_file:
    json.dump(report, json_file, ensure_ascii=False, indent=4)
