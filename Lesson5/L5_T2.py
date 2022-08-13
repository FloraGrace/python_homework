'''Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.'''

with open('L5_T2.txt', 'r', encoding='UTF-8') as my_file:
    file_lines = my_file.readlines()
    print(f"Всего строк: {len(file_lines)}")
    for i, el in enumerate(file_lines):
        words = el.split(' ')
        print(f"Слов в строке {i + 1} - {len(words)}")
