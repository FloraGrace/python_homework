# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input('Время в секундах '))
hour = user_seconds // 3600
remainder = user_seconds - hour*3600
minutes = remainder//60
seconds = remainder - minutes*60
print(f'{hour:02}:{minutes:02}:{seconds:02}')

