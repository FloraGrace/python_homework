'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

from random import randint

with open('L5_T5.txt', 'w', encoding='UTF-8') as my_file:
    my_list = [randint(1, 30) for _ in range(1, 5)]
    print(" ".join(map(str, my_list)), file=my_file) # сохраняем в файл

with open('L5_T5.txt', 'r', encoding='UTF-8') as my_file:
    print(f'Сумма числе в файле равна {sum(list(map(int, my_file.read().strip().split())))}')


