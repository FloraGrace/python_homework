'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.'''


with open('text_4.txt', 'r', encoding='UTF-8') as file_en:
    text_en = file_en.read()

dict_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
text_ru = text_en
for en, ru in dict_rus.items():
    text_ru = text_ru.replace(en, ru)

with open('text_4_ru.txt', 'w', encoding='UTF-8') as file_ru:
    file_ru.writelines(text_ru)

#========= вариант 2 ========================================================

with open('text_4.txt', 'r', encoding='UTF-8') as file_en:
    dict_en = {line.split()[2]: line.split()[0] for line in file_en}
    dict_rus = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
    dict_en.update(dict_rus)

with open('text_4_rus.txt','w', encoding='UTF-8') as file_ru:
    for key,val in dict_en.items():
        file_ru.write('{} - {}\n'.format(val,key))
