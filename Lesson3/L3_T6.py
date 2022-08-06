'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().
'''

def int_func(word):
    '''проверка вводимых слов на написание латиницей и обязательный перевод первой буквы в заглавную'''
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else None

my_str = input('Введите слова через пробел ').split()
result = ()
new_result = []
for i in my_str:
    result = int_func(i)
    if not result == None:
        new_result.append(result)

print(new_result)
